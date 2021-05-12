<template>
  <div class="container">
    <h1 class="mt-4 mb-4">
      {{ course.title }}
    </h1>
    <h6>
      {{ course.description }}
    </h6>

    <h3>Modules</h3>

    <p v-if="isEmptyModules">No content</p>
    <ol v-else>
      <li v-for="module in course.modules" :key="module.id">
        <b-link
          v-if="isAlreadyEnrolled || isCourseOwner"
          :href="`/pitch/courses/${course.id}/modules/${module.id}`"
          class="card-link"
          >{{ module.title }}</b-link
        >
        <span v-else>{{ module.title }}</span>
      </li>
    </ol>

    <h3>Tests</h3>
    <p v-if="isEmptyTests">No content</p>
    <ol v-else>
      <li v-for="test in course.tests" :key="test.id">
        <b-link
          v-if="isAlreadyEnrolled"
          :href="`/pitch/courses/${course.id}/tests/${test.id}`"
          class="card-link"
          >{{ test.title }}</b-link
        >
        <span v-else>{{ test.title }}</span>
      </li>
    </ol>

    <b-button v-if="!isAlreadyEnrolled && !isCourseOwner" @click="enroll" svariant="secondary"
      >enroll</b-button
    >
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "CourseDetail",
  data() {
    return {
      course: {},
      isAlreadyEnrolled: false,
      isCourseOwner: false,
      isEmptyModules: false,
      isEmptyTests: false
    };
  },
  components: {},
  mounted() {
    let currentProfileId = localStorage.getItem("profileId");

    axios
      .get(`http://127.0.0.1:8000/pitch/courses/${this.$route.params.id}`)
      .then((response) => {
        this.course = response.data;
        console.log(response.data);
        this.isEmptyModules = this.course.modules.length == 0;
        this.isEmptyTests = this.course.tests.length == 0;
        this.isAlreadyEnrolled = this.course.students.some(s => s.id == currentProfileId);
        this.isCourseOwner = this.course.teacher.id == currentProfileId;
      });
  },
  methods: {
    enroll() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .post(
          `http://127.0.0.1:8000/pitch/courses/${this.course.id}/enroll/`,
          {},
          options
        )
        .then((response) => {
          console.log(response.data);
          this.isAlreadyEnrolled = true;
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>
