<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Add material</h1>

    <b-form-group id="input-group-3" label-for="input-3">
      <b-form-input
        id="input-3"
        v-model="form.text"
        type="text"
        placeholder="Enter material"
        required
      ></b-form-input>
    </b-form-group>

    <div class="row mt-4 justify-content-center">
      <b-button v-on:click="addMaterial" variant="secondary">Save</b-button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        text: "",
        module: this.$route.params.moduleId,
      },
    };
  },
  methods: {
    addMaterial() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .post("http://127.0.0.1:8000/pitch/materials/", this.form, options)
        .then((response) => {
          console.log(response.data);
          this.$router.push(`/pitch/teacher`);
        })
        .catch((error) => console.log(error));
    },
  },
};
</script>