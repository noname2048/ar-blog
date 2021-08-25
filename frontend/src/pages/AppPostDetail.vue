<template>
  <v-app id="inspire">

    <MainMenu></MainMenu>

    <v-main>
      <PostDetail></PostDetail>
    </v-main>
    <v-footer app>
      <span>&copy; 2021</span>
    </v-footer>
  </v-app>
</template>

<script>
import MainMenu from '../components/MainMenu.vue';
import PostDetail from '../components/PostDetail.vue';

export default {
  components: { MainMenu, PostDetail },
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
