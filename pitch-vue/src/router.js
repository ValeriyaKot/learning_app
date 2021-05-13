import Vue from 'vue'
import Router from 'vue-router'
import Courses from './views/Courses.vue'
import CourseDetail from './views/CourseDetail.vue'
import CheckTest from './views/CheckTest.vue'
import Home from './views/Home.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'
import ChangePassword from './views/ChangePassword.vue'
import Profile from './views/Profile.vue'
import TestResults from './views/TestResults.vue'
import AddCourse from './views/AddCourse.vue'
import StudentCourses from './views/StudentCourses.vue'
import AddModule from './views/AddModule.vue'
import Module from './views/Module.vue'
import AddTest from './views/AddTest.vue'
import AddQuestions from './views/AddQuestions.vue'
import TeacherCourses from './views/TeacherCourses.vue'
import AddMaterial from './views/AddMaterial.vue'


Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/pitch',
      component:Home
    },
    {
      path: '/pitch/profile',
      component:Profile
    },
    {
      path: '/pitch/login',
      component: Login
    },
    {
      path: '/pitch/register',
      component: Register
    },
    {
      path: '/pitch/change-password',
      component: ChangePassword
    },
    {
      path: '/pitch/courses',
      component: Courses,
    },
    {
      path: '/pitch/courses/add',
      component: AddCourse,
    },
    {
      path: '/pitch/courses/:id',
      component: CourseDetail 
    },
    {
      path: '/pitch/courses/:id/add-test',
      component: AddTest
    },
    {
      path: '/pitch/courses/:id/add-module',
      component: AddModule
    },
    {
      path: '/pitch/courses/:id/modules/:moduleId',
      component: Module
    },
    {
      path: '/pitch/courses/:id/modules/:moduleId/add-material',
      component: AddMaterial
    },
    {
      path: '/pitch/courses/:id/tests/:testId',
      component: CheckTest
    },
    {
      path: '/pitch/courses/:id/tests/:testId/add-questions',
      component: AddQuestions
    },
    {
      path: '/pitch/profile/tests-results',
      component: TestResults
    },
    {
      path: '/pitch/profile/courses',
      component: StudentCourses
    },
    {
      path: '/pitch/teacher',
      component: TeacherCourses
    },
  ]
})