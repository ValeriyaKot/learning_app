<template>
  <div class="container">
    <h1 class="text-center mb-4 mt-4">
      {{ module.title }}
    </h1>
    <ol>
      <li v-for="material in module.materials" :key="material.id">
        <p>{{ material.text }}</p>
      </li>
    </ol>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Module",
  data() {
    return {
      module: {},
    };
  },
  mounted() {
    let token = JSON.parse(localStorage.getItem("token"))["access"];
    let options = {
      headers: { Authorization: "Bearer " + token },
    };
    axios
      .get(
        `http://127.0.0.1:8000/pitch/modules/${this.$route.params.moduleId}`,
        options
      )
      .then((response) => {
        this.module = response.data;
        console.log(response);
      });
  },
};
</script>