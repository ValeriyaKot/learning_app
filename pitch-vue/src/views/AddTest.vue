<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Add test</h1>

    <b-form v-if="show">
      <b-form-group>
        <b-form-group id="input-group-1" label="Title" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="form.title"
            type="text"
            placeholder="Enter module title"
            required
          ></b-form-input>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Attempts number"
          label-for="input-2"
        >
          <b-form-input
            id="input-2"
            v-model="form.attempts_number"
            type="number"
            min="1"
            placeholder="Enter an attempts number"
          ></b-form-input>
        </b-form-group>
      </b-form-group>
    </b-form>
    <div class="row mt-4 mb-4 justify-content-center">
      <b-button v-on:click="addTest" variant="secondary">Next</b-button>
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
        attempts_number: "",
        course: this.$route.params.id,
      },
      show: true,
    };
  },
  methods: {
    addTest() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      if (
        this.form.attempts_number == "" ||
        parseInt(this.form.attempts_number, 10) < 1
      ) {
        this.form.attempts_number = null;
      }
      console.log(this.form);
      axios
        .post("http://127.0.0.1:8000/pitch/tests/", this.form, options)
        .then((response) => {
          console.log(response.data);
          this.$router.push(
            `/pitch/courses/${this.course}/tests/${response.data.id}/add-questions`
          );
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>