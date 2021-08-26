<template>
  <v-container class="grey lighten-5" fluid>
    <v-row align="center" justify="center">
      <v-col cols="12" sm="12">
        <h1>Post title here</h1>
        <p>2020-07-10, written by swook</p>
      </v-col>
    </v-row>

    <v-row align="start" justify="center">
      <v-col cols="12" sm="8" lg="7">
        <v-card class="pa-2" outlined tile>
          <p>
            I study Vue.js and Django<br /><br /><br /><br /><br /><br /><br /><br /><br /><br />
            And more Vuetify.
          </p>
          <div>
            <strong>TAGS:</strong>
            <v-chip class="ma-2" color="success" outlined>
              python
            </v-chip>
            <v-chip class="ma-2" color="success" outlined>
              django
            </v-chip>
          </div>
        </v-card>
      </v-col>

      <v-col cols="12" sm="4" lg="3">
        <v-card class="pa-2 mb-5" tile>
          <p>prev post</p>
          <h2>Previous title here</h2>
        </v-card>
        <v-card class="pa-2 mb-5" tile>
          <p>next post</p>
          <h2>Next title here</h2>
        </v-card>
        <v-card class="pa-2" outlined tile>
          <h2>Tag cloud</h2>
          <v-chip class="ma-2" color="green" text-color="white">
            <v-avatar class="green darken-4">
              1
            </v-avatar>
            python
          </v-chip>
          <v-chip class="ma-2" color="green" text-color="white">
            <v-avatar class="green darken-4">
              1
            </v-avatar>
            django
          </v-chip>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "HelloWorld",

  data: () => ({
    ecosystem: [
      {
        text: "vuetify-loader",
        href: "https://github.com/vuetifyjs/vuetify-loader",
      },
      {
        text: "github",
        href: "https://github.com/vuetifyjs/vuetify",
      },
      {
        text: "awesome-vuetify",
        href: "https://github.com/vuetifyjs/awesome-vuetify",
      },
    ],
    importantLinks: [
      {
        text: "Documentation",
        href: "https://vuetifyjs.com",
      },
      {
        text: "Chat",
        href: "https://community.vuetifyjs.com",
      },
      {
        text: "Made with Vuetify",
        href: "https://madewithvuejs.com/vuetify",
      },
      {
        text: "Twitter",
        href: "https://twitter.com/vuetifyjs",
      },
      {
        text: "Articles",
        href: "https://medium.com/vuetify",
      },
    ],
    whatsNext: [
      {
        text: "Explore components",
        href: "https://vuetifyjs.com/components/api-explorer",
      },
      {
        text: "Select a layout",
        href: "https://vuetifyjs.com/getting-started/pre-made-layouts",
      },
      {
        text: "Frequently Asked Questions",
        href:
          "https://vuetifyjs.com/getting-started/frequently-asked-questions",
      },
    ],
  }),
};
</script>
