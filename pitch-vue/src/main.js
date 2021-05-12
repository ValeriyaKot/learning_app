import Vue from 'vue'
import App from './App.vue'
import router from './router'
import axios from 'axios'
import VeeValidate from 'vee-validate';
import { library } from '@fortawesome/fontawesome-svg-core';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import {
  faHome,
  faUser,
  faUserPlus,
  faSignInAlt,
  faSignOutAlt
} from '@fortawesome/free-solid-svg-icons';


import { BootstrapVue, IconsPlugin } from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
library.add(faHome, faUser, faUserPlus, faSignInAlt, faSignOutAlt);
Vue.use(BootstrapVue)
Vue.use(IconsPlugin)
Vue.use(VeeValidate);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.config.productionTip = false
Vue.prototype.$http = axios;

const token = localStorage.getItem('token')
if (token) {
  Vue.prototype.$http.defaults.headers.common['Authorization'] = token
}

new Vue({
  el: '#app',
  router,
  render: h => h(App)
}).$mount('#app');
