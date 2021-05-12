<template>
  <div class="container">
    <h1 class="text-center my-4">Courses</h1>
    <div>
      <CourseItem v-for="course in courses" :key="course.id" :course="course" />
    </div>
  </div>
</template>

<script>
import CourseItem from "../components/CourseItem.vue";
import axios from "axios";

export default {
  name: "Courses",
  data() {
    return {
      courses: [],
    };
  },
  components: {
    CourseItem,
  },
  mounted() {
    axios
      .get("http://127.0.0.1:8000/pitch/courses")
      .then((response) => (this.courses = response.data));
  },
};
</script>