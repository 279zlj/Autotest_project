// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
require('./mock/mock')

Vue.config.productionTip = false

Vue.prototype.$axios=axios
Vue.prototype.$http=axios
//Vue.prototype.HOME='/api'

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
