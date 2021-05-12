<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Tests results</h1>
      <ResultItem v-for="(result, index) in results"
        :key="index"
        :index="index"
        :result="result"/>
  </div>
</template>

<script>
import ResultItem from "../components/ResultItem.vue";
import axios from "axios";

export default {
  name: "Results",
  data() {
    return {
      results: [],
    };
  },
  components: {
    ResultItem,
  },
  mounted() {
    let token = JSON.parse(localStorage.getItem("token"))["access"];
    let options = {
      headers: { Authorization: "Bearer " + token },
    };
    axios
      .get("http://127.0.0.1:8000/pitch/results", options)
      .then((response) => (this.results = response.data));
  },
};
</script>