<template>
  <div class="container">
    <h1 class="text-center mb-4 mt-4">Courses</h1>
    <TeacherCourseItem
      v-for="(teacherCourse, index) in teacherCourses"
      :key="teacherCourse.id"
      :index="index"
      :teacherCourse="teacherCourse"
    />
    <div class="row mt-4 mb-4 justify-content-center">
      <b-button variant="secondary" href="/pitch/courses/add"
        >Add course</b-button
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";
import TeacherCourseItem from "../components/TeacherCourseItem.vue";

export default {
  name: "TeacherCourses",
  data() {
    return {
      teacherCourses: [],
    };
  },
  components: {
    TeacherCourseItem,
  },
  mounted() {
    let token = JSON.parse(localStorage.getItem("token"))["access"];
    let options = {
      headers: { Authorization: "Bearer " + token },
    };

    axios
      .get("http://127.0.0.1:8000/pitch/teacher/courses", options)
      .then((response) => (this.teacherCourses = response.data));
  },
};
</script>
