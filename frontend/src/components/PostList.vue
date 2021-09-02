<template>
  <v-container>
    <v-data-table
      :headers="headers"
      :items="posts"
      sort-by="name"
      class="elevation-1"
      :items-per-page="10"
      @click:row="serverPage"
    >
      <template v-slot:top>
        <v-toolbar flat>
          <v-toolbar-title
            >Post List<span v-if="tagname" class="body-1 font-italic ml-3"
              >(with {{ tagname }} tagged)</span
            ></v-toolbar-title
          >
          <v-divider class="mx-4" inset vertical></v-divider>
          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            dark
            class="mb-2"
            @click.stop="dialogOpen('create', {})"
          >
            New Post
          </v-btn>
        </v-toolbar>
      </template>

      <template v-slot:item.actions="{ item }">
        <v-icon small class="mr-2" @click.stop="dialogOpen('update', item)">
          mdi-pencil
        </v-icon>
        <v-icon small @click.stop="deletePost(item)">
          mdi-delete
        </v-icon>
      </template>

      <template v-slot:no-data>
        <v-btn color="primary" @click="fetchPostList">
          Reset
        </v-btn>
      </template>
    </v-data-table>

    <v-dialog v-model="dialog" max-width="800px">
      <v-card>
        <v-card-title>
          <span class="text-h5">{{ formTitle }}</span>
        </v-card-title>

        <v-card-text>
          <v-form id="post-form" ref="postForm">
            <v-text-field
              label="ID"
              name="id"
              v-model="editedItem.id"
              readonly
            ></v-text-field>
            <v-text-field
              label="TITLE"
              name="title"
              v-model="editedItem.title"
            ></v-text-field>
            <v-text-field
              label="DESCRIPTION"
              name="description"
              v-model="editedItem.description"
            ></v-text-field>
            <v-textarea
              outlined
              label="CONTENT"
              name="content"
              v-model="editedItem.content"
            ></v-textarea>
            <v-text-field
              label="OWNER"
              name="owner"
              v-model="editedItem.owner"
              readonly
            ></v-text-field>
            <v-text-field
              label="TAGS"
              name="tags"
              v-model="editedItem.tags"
            ></v-text-field>
          </v-form>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="cancel()">
            Cancel
          </v-btn>
          <v-btn color="blue darken-1" text @click="save()">
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="dialogDelete" max-width="500px">
      <v-card>
        <v-card-title class="text-h5"
          >Are you sure you want to delete this item?</v-card-title
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="blue darken-1" text @click="cancel()">Cancel</v-btn>
          <v-btn color="blue darken-1" text @click="save()">Save</v-btn>
          <v-spacer></v-spacer>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import axios from "axios";
import EventBus from "./event_bus";

export default {
  data: () => ({
    dialog: false,
    dialogDelete: false,
    headers: [
      {
        text: "ID",
        align: "start",
        sortable: false,
        value: "id",
      },
      { text: "제 목", value: "title" },
      { text: "요약", value: "description" },
      { text: "수정일", value: "modify_dt" },
      { text: "작성자", value: "owner" },
      { text: "Actions", value: "actions", sortable: false },
    ],
    tagname: "",
    posts: [],
    editedIndex: -1,
    editedItem: {},
    actionKind: "",
    me: { username: "Anonymous" },
  }),

  computed: {
    formTitle() {
      // return this.editedIndex === -1 ? "New Item" : "Edit Item";
      if (this.actionKind === "create") return "Create Item";
      else return "Update Item";
    },
  },

  created() {
    const params = new URL(location).searchParams;
    this.tagname = params.get("tagname");
    this.fetchPostList();

    EventBus.$on("me_change", (val) => {
      this.me = val;
    });
  },

  methods: {
    async fetchPostList() {
      console.log("fetchPostList()...", "tagname", this.tagname);

      let getUrl = "";
      if (this.tagename) getUrl = `/api/post/list/?tagname=${this.tagname}`;
      else getUrl = "/api/post/list/";

      try {
        const res = await axios.get(getUrl);
        console.log("POST LIST GET RES", res);
        this.posts = res.data;
      } catch (err) {
        console.error("POST LIST GET ERR", err);
        alert(err.response.status + " " + err.response.statusText);
      }
    },

    serverPage(item) {
      console.log("serverPage()...", item);
      location.href = `/blog/post/${item.id}`;
    },

    dialogOpen(actionKind, item) {
      console.log("dialogOpen()...", actionKind);
      this.actionKind = actionKind;
      if (actionKind === "create") {
        this.editedIndex = -1;
        this.editedItem = {};
      } else {
        this.editedIndex = this.posts.indexOf(item);
        this.editedItem = Object.assign({}, item); // shallow merge
      }
      this.dialog = true;
    },

    cancel() {
      console.log("cancel()...");
      this.dialog = false;
    },

    save() {
      console.log("save()...");
      if (this.actionKind === "create") this.createPost();
      else if (this.actionKind === "update") this.updatePost();
      else {
        console.log("save() gets wrong arguments");
        alert("save() gets wrong arguments");
      }
      this.dialog = false;
    },

    async createPost() {
      console.log("createPost()...");
      const postData = new FormData(document.getElementById("post-form"));
      try {
        const res = await axios.post("/api/post/create/", postData);
        console.log("CREATEPOST POST RES", res);
        this.posts.push(res.data);
      } catch (err) {
        console.error("CREATEPOST POST ERR.RESPONSE", err.response);
        const { status, statusText } = err.response;
        alert(status + " " + statusText);
      }
    },

    async updatePost() {
      console.log("updatePost()...");
      const postData = new FormData(document.getElementById("post-form"));
      postData.set('owner', this.me.id);
      try {
        const res = await axios.post(
          `/api/post/${this.editedItem.id}/update/`,
          postData
        );
        console.log("CREATEPOST POST RES", res);
        this.posts.splice(this.editedIndex, 1, res.data);
      } catch (err) {
        console.error("CREATEPOST POST ERR.RESPONSE", err.response);
        const { status, statusText } = err.response;
        alert(status + " " + statusText);
      }
    },

    async deletePost(item) {
      console.log("deletePost()...", item);
      if (!confirm("Are you sure to delete?")) return;
      try {
        const res = await axios.delete(`/api/post/${item.id}/delete`);
        console.log("DELETEPOST DELETE RES", res);
        const index = this.posts.indexOf(item);
        this.posts.splice(index, 1);
      } catch (err) {
        console.log("DLETEPOST DELETE ERR.RESPONSE", err.response);
        const { status, statusText } = err.response;
        alert(status + " " + statusText);
      }
    },
  },
};
</script>

<style scoped>
.v-data-table >>> tbody > tr {
  cursor: pointer;
}
</style>
