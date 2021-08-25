<template>
  <v-app id="inspire">

    <MainMenu></MainMenu>

    <v-main>
      <PostList></PostList>
    </v-main>
    <v-footer app>
      <span>&copy; 2021</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from '../components/MainMenu.vue';
import PostList from "../components/PostList.vue";

export default {
  components: { MainMenu, PostList },
  data: () => ({
    // drawer: null,
    items: [
      { title: "Dashboard", icon: "mdi-view-dashboard" },
      { title: "Photos", icon: "mdi-image" },
      { title: "About", icon: "mdi-help-box" },
    ],
  }),
};
</script>
