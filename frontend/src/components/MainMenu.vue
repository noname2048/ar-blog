<template>
  <div>
    <v-navigation-drawer v-model="drawer" app clipped>
      <v-list dense nav>
        <v-list-item v-for="item in items" :key="item.title" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar app clipped-left color="indigo" dark>
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>

      <v-toolbar-title>Vue.js - Django web Porgramming</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn text href="/">Home</v-btn>
      <v-btn text href="/blog/post/list/">blog</v-btn>
      <v-btn text href="/admin/">Admin</v-btn>
      <v-btn text>/</v-btn>
      <v-btn text href="/">Home</v-btn>
      <v-btn text href="/post_list.html">PostList</v-btn>
      <v-btn text href="/post_detail.html">PostDetail</v-btn>

      <v-spacer></v-spacer>

      <!-- <v-menu offset-y left bottom> -->
      <v-menu offset-y>
        <template v-slot:activator="{ on, attrs }">
          <v-btn text v-bind="attrs" v-on="on">
            <v-icon>mdi-account</v-icon>
            Anonymous
            <v-icon>mdi-dots-vertical</v-icon>
          </v-btn>
        </template>

        <v-list>
          <v-list-item @click="dialog.login = true">
            <v-list-item-title>Login</v-list-item-title>
          </v-list-item>
          <v-list-item @click="dialog.register = true">
            <v-list-item-title>Register</v-list-item-title>
          </v-list-item>
          <v-list-item @click="dialog.logout = true">
            <v-list-item-title>Logout</v-list-item-title>
          </v-list-item>
          <v-list-item @click="dialog.changePassword = true">
            <v-list-item-title>Password change</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>

    <!-- login dialog -->
    <v-dialog v-model="dialog.login" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar color="primary" dark flat>
          <v-toolbar-title>Login form</v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          <v-form id="login-form">
            <v-text-field
              label="Username"
              name="username"
              prepend-icon="mdi-account"
              type="text"
            ></v-text-field>

            <v-text-field
              label="Password"
              name="password"
              prepend-icon="mdi-lock"
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="grey" @click="cancel('login')">Cancel</v-btn>
          <v-btn color="primary" class="mr-5" @click="save('login')">Login</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- register dialog -->
    <v-dialog v-model="dialog.register" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar color="success" dark flat>
          <v-toolbar-title>Register Form</v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          <v-form>
            <v-text-field
              label="Username"
              name="username"
              prepend-icon="mdi-account"
              type="text"
            ></v-text-field>

            <v-text-field
              label="Password"
              name="password1"
              prepend-icon="mdi-lock"
              type="password"
            ></v-text-field>
            <v-text-field
              label="Password Confirm"
              name="password2"
              prepend-icon="mdi-lock"
              type="password"
            ></v-text-field>

          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="grey" @click="dialog.register = false">Cancel</v-btn>
          <v-btn color="success" class="mr-5" @click="dialog.register = false">Register</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
    
    <!-- password change dialog -->
    <v-dialog v-model="dialog.changePassword" max-width="600">
      <v-card class="elevation-12">
        <v-toolbar color="warning" dark flat>
          <v-toolbar-title>Change Password Form</v-toolbar-title>
        </v-toolbar>
        <v-card-text>
          <v-form>

            <v-text-field
              label="Old Password"
              name="old_password"
              prepend-icon="mdi-lock"
              type="password"
            ></v-text-field>
            <v-text-field
              label="New Password"
              name="new_password1"
              prepend-icon="mdi-lock"
              type="password"
            ></v-text-field>
            <v-text-field
              label="Confirm New Password"
              name="new_password2"
              prepend-icon="mdi-lock"
              type="password"
            ></v-text-field>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn text color="grey" @click="dialog.changePassword = false">Cancel</v-btn>
          <v-btn color="warning" class="mr-5" @click="dialog.changePassword = false">change password</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

  </div>
</template>

<script>
import axios from 'axios';

axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFToken";

export default {
  data: () => ({
    drawer: null,
    dialog: {
      login: false,
      register: false,
      logout: false,
      pwdchg: false,
    },
    me: {},
    items: [
      { title: "Dashboard", icon: "mdi-view-dashboard" },
      { title: "Photos", icon: "mdi-image" },
      { title: "About", icon: "mdi-help-box" },
    ],
  }),

  methods: {
    cancel(kind) {
      console.log("cancel()...", kind);
      if (kind === 'login') this.dialog.login = false;
      else if (kind === 'register') this.dialog.register = false;
      else if (kind === 'pwdchg') this.dialog.pwdchg = false;
      else { console.log("wrong cancel kind")}
    },

    save(kind) {
      console.log("save()...", kind);
      if (kind === 'login') {
        this.login();
        this.dialog.login = false;
      } else if (kind === 'register') {
        this.register();
        this.dialog.register = false;
      } else if (kind === 'pwdchg') {
        this.pwdchg();
        this.dialog.pwdchg = false;
      }
    },

    async login() {
      console.log('login()...');
      const postData = new FormData(document.getElementById('login-form'));
      try {
        const res = await axios.post('/api/login/', postData);
        console.log("LOGIN POST RES", res);
        alert(`user ${res.data.username} login OK`);
        this.me = res.data;
      } catch (err) {
        console.log("LOGIN POST ERR.RESPONSE", err.response);
        alert("login NOK");
      }

    }


  }
};
</script>

<style></style>
