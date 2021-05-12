<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Your сourses</h1>
    <div>
      <StudentCourseItem
        v-for="(studentCourse, index) in studentCourses"
        :key="studentCourse.id"
        :studentCourse="studentCourse"
        :index="index"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import StudentCourseItem from "../components/StudentCourseItem.vue";
export default {
  name: "StudentCourses",
  data() {
    return {
      studentCourses: [],
    };
  },
  components: {
    StudentCourseItem,
  },
  mounted() {
    let token = JSON.parse(localStorage.getItem("token"))["access"];
    let options = {
      headers: { Authorization: "Bearer " + token },
    };
    axios
      .get("http://127.0.0.1:8000/pitch/student/courses", options)
      .then((response) => (this.studentCourses = response.data));
  },
};
</script>