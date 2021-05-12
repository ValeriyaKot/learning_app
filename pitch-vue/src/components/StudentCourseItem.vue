<template>
  <div class="container">
    <div class="row py-2 border-top">
      <div class="col-8">
        {{ studentCourse.title }}
      </div>
      <div class="col-2">
        <b-button v-b-toggle="moduleCollapseId" variant="outline-secondary"
          >Modules</b-button
        >
      </div>

      <div class="col-2">
        <b-button v-b-toggle="testCollapseId" variant="outline-secondary"
          >Tests</b-button
        >
      </div>
    </div>

    <b-collapse :id="moduleCollapseId" class="mt-2">
    <p v-if="isEmptyModules">No content</p>
      <ol v-else>
        <li v-for="module in studentCourse.modules" :key="module.id">
          <div class="m-2">
            <h6>{{ module.title }}</h6>
            <ul
              class="my-2"
              v-for="material in module.materials"
              :key="material.id"
            >
              <li>
                {{ material.text }}
              </li>
            </ul>
          </div>
        </li>
      </ol>
    </b-collapse>

    <b-collapse :id="testCollapseId" class="my-2">
    <p v-if="isEmptyTests">No content</p>
      <div v-else class="container">
        <StudentTestItem
          v-for="(test, index) in tests"
          :courseId="studentCourse.id"
          :index="index"
          :key="index"
          :test="test"
        />
      </div>
    </b-collapse>
  </div>
</template>

<script>
import StudentTestItem from "../components/StudentTestItem.vue";
import axios from "axios";

export default {
  props: {
    studentCourse: Object,
    index: Number,
  },
  data() {
    return {
      tests: [],
      isEmptyModules: false,
      isEmptyTests: false,
    };
  },
  components: {
    StudentTestItem,
  },
  computed: {
    moduleCollapseId: function () {
      return `module-collapse-${this.index}`;
    },
    testCollapseId: function () {
      return `tests-collapse-${this.index}`;
    },
  },
  mounted() {
    let token = JSON.parse(localStorage.getItem("token"))["access"];

    let options = {
      headers: { Authorization: "Bearer " + token },
    };
    axios
      .get(
        `http://127.0.0.1:8000/pitch/course-tests/${this.studentCourse.id}/tests`,
        options
      )
      .then((response) => {
        this.tests = response.data;
        this.isEmptyTests = this.tests.length == 0;
        this.isEmptyModules = this.studentCourse.modules.length == 0;
      });
  },
};
</script>
