<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Add course</h1>

    <b-form>
      <b-form-group>
        <b-form-group id="input-group-1" label="Title" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="form.title"
            type="text"
            placeholder="Enter course title"
            required
          ></b-form-input>
        </b-form-group>
        <b-form-group
          id="input-group-2"
          label="Description"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.description"
            type="text"
            placeholder="Enter course description"
            required
          ></b-form-input>
        </b-form-group>
      </b-form-group>
    </b-form>
    <div class="row mt-4 mb-4 justify-content-center">
      <b-button v-on:click="addCourse" variant="secondary">Next</b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      form: {
        title: "",
        description: "",
      },
    };
  },
  methods: {
    addCourse() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .post("http://127.0.0.1:8000/pitch/courses/", this.form, options)
        .then((response) => {
          console.log(response.data);
          this.$router.push(`/pitch/courses/${response.data.id}/add-module`);
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>