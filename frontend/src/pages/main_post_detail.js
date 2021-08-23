import AppPostDetail from './AppPostDetail.vue'
import Vue from 'vue'
import vuetify from '../plugins/vuetify'

Vue.config.productionTip = false

new Vue({
  vuetify,
  render: h => h(AppPostDetail)
}).$mount('#app')
