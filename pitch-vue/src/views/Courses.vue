<template>
    <div class="text-center">
        <h1>Courses</h1>
        <div>
            <CourseItem
                v-for="course in courses" :key="course.id"
                v-bind:course="course"
            />
        </div>
        <router-view></router-view>
    </div>
</template>

<script>
import CourseItem from '../components/CourseItem.vue'
import axios from 'axios'

export default {
    name: 'Courses',
  data() {
      return {
          courses: []
      }
  },
  components: {
    CourseItem
  },
  mounted() {
    axios
        .get('http://127.0.0.1:8000/pitch/courses')
        .then(response => (this.courses = response.data))

    } 
  }
</script>

<style>
</style>