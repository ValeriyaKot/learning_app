<template>
  <div class="container">
    <div class="row py-2 border-top">
      <div class="col-6">
        {{ teacherCourse.title }}
      </div>

      <div class="col-2">
        <b-button
          v-b-toggle="testCollapseId"
          variant="outline-secondary"
          class="btn-block"
          >Tests</b-button
        >
      </div>
      <div class="col-2">
        <b-button
          v-b-toggle="moduleCollapseId"
          variant="outline-secondary"
          class="btn-block"
          >Modules</b-button
        >
      </div>
      <div class="col-2">
        <b-button variant="danger" v-on:click="deleteCourse" class="btn-block"
          >Delete</b-button
        >
      </div>
    </div>

    <b-collapse :id="moduleCollapseId">
      <div class="container">
        <div class="row my-2">
          <div class="col-12">
            <ol>
              <li
                v-for="(module, index) in teacherCourse.modules"
                :index="index"
                :key="module.id"
              >
                <div class="row pt-4 border-top">
                  <div class="col-9">
                    <h6>{{ module.title }}</h6>
                  </div>
                  <div class="col-3 text-right">
                    <b-button
                      size="sm"
                      variant="danger"
                      v-on:click="deleteModule(module.id, index)"
                      >Delete module</b-button
                    >
                  </div>
                </div>

                <div class="row my-2">
                  <div class="col-12">
                    <ul>
                      <li
                        v-for="material in module.materials"
                        :key="material.id"
                        class="container"
                      >
                        <div class="row my-3">
                          <div class="col-12">
                            {{ material.text }}
                          </div>
                        </div>

                        <div class="row my-3 justify-content-end">
                          <div class="col-3">
                            <b-button
                              size="sm"
                              variant="outline-danger"
                              v-on:click="deleteModule(module.id, index)"
                              class="btn-block"
                              >Delete material</b-button
                            >
                          </div>
                        </div>
                      </li>
                    </ul>
                  </div>
                </div>

                <div class="row my-4 justify-content-center">
                  <b-button
                    size="sm"
                    variant="secondary"
                    :href="`/pitch/courses/${teacherCourse.id}/modules/${module.id}/add-material`"
                    >Add material</b-button
                  >
                </div>
              </li>
            </ol>
          </div>
        </div>

        <div class="row my-4 justify-content-start">
          <div class="col-3">
            <b-button
              variant="secondary"
              :href="`/pitch/courses/${teacherCourse.id}/add-module`"
              class="btn-block"
              >Add module</b-button
            >
          </div>
        </div>
      </div>
    </b-collapse>

    <b-collapse :id="testCollapseId" class="my-2">
      <div class="container">
        <TestItem
          v-for="(test, index) in tests"
          :courseId="teacherCourse.id"
          :index="index"
          :key="index"
          :test="test"
        />
        <div class="row my-4 justify-content-start">
          <div class="col-3">
            <b-button
              variant="secondary"
              :href="`/pitch/courses/${teacherCourse.id}/add-test`"
              class="mt-2"
              >Add test</b-button
            >
          </div>
        </div>
      </div>
    </b-collapse>
  </div>
</template>

<script>
import TestItem from "../components/TestItem.vue";
import axios from "axios";

export default {
  props: {
    teacherCourse: Object,
    index: Number,
  },
  data() {
    return {
      tests: [],
    };
  },
  components: {
    TestItem,
  },
  computed: {
    moduleCollapseId: function () {
      return `module-collapse-${this.index}`;
    },
    testCollapseId: function () {
      return `test-collapse-${this.index}`;
    },
  },
  mounted() {
    let token = JSON.parse(localStorage.getItem("token"))["access"];
    let options = {
      headers: { Authorization: "Bearer " + token },
    };
    axios
      .get(
        `http://127.0.0.1:8000/pitch/course-tests/${this.teacherCourse.id}/tests`,
        options
      )
      .then((response) => (this.tests = response.data));
  },
  methods: {
    deleteModule: function (moduleId, index) {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .delete(`http://127.0.0.1:8000/pitch/modules/${moduleId}`, options)
        .then((response) => {
          if (response.status == 204) {
            this.teacherCourse.modules.splice(index, 1);
          }
        });
    },
    deleteCourse() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .delete(
          `http://127.0.0.1:8000/pitch/courses/${this.teacherCourse.id}`,
          options
        )
        .then((response) => {
          if (response.status == 204) {
            this.$router.go("/pitch/teacher");
          }
        });
    },
  },
};
</script>
