import Vue from 'vue'
import Router from 'vue-router'
import Courses from './views/Courses.vue'
import CourseDetail from './views/CourseDetail.vue'
import Test from './views/Test.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/pitch',
      component: () => import('./views/Home.vue')
    },
    {
      path: '/pitch/login',
      component: () => import('./views/Login.vue')
    },
    {
      path: '/pitch/courses',
      component: Courses,
    },
    {
      path: '/pitch/courses/:id',
      component: CourseDetail 
    },
    {
      path: '/pitch/tests/:id',
      component: Test,
      meta: { 
        requiresAuth: true
      }
    }
  ]
})