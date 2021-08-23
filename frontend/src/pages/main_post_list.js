import AppPostList from './AppPostList.vue'
import Vue from 'vue'
import vuetify from '../plugins/vuetify'

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(AppPostList)
}).$mount('#app')
