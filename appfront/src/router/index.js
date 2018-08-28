import Vue from 'vue'
import Router from 'vue-router'
import axios from 'axios'
import HelloWorld from '@/components/HelloWorld'
import search from '@/components/search'
import table_data from '@/components/table_data'
import Error from '@/components/Error'

import '@/assets/js/jquery-3.3.1.min.js';
import '@/assets/css/bootstrap.min.css';
import '@/assets/js/bootstrap.min.js';
import '@/assets/js/nav.js';

import '@/assets/js/index.js';


Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'HelloWorld',
      components: {
        default:HelloWorld,
        right:table_data

      }
    },
    {
      path:'/search',
      name:'search',

      components:{
        default:HelloWorld,
        right:search
      }
    },
    {
      path:'/table_data',
      name:'table_data',
      components:table_data
    },
    {
      path:'*',
      component:Error
    },
  ]
})
