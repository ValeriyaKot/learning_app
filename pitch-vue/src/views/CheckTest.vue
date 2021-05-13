<template>
  <div>
    <div class="container my-4">
      <h1>{{ test.title }}</h1>
      <QuestionItem
        v-for="question in test.questions"
        :key="question.id"
        :question="question"
        :answers="answers"
      />
      <div class="my-4">
        <b-button v-on:click="check" type="submit" variant="secondary"
          >Check</b-button
        >
      </div>
      <h3>Test result: {{ result }}</h3>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import QuestionItem from "../components/QuestionItem.vue";
export default {
  name: "Test",
  data() {
    return {
      test: {},
      answers: {},
      result: "",
    };
  },
  components: {
    QuestionItem,
  },
  mounted() {
    let token = JSON.parse(localStorage.getItem("token"))["access"];

    let options = {
      headers: { Authorization: "Bearer " + token },
    };
    axios
      .get(
        `http://127.0.0.1:8000/pitch/tests/${this.$route.params.testId}`,
        options
      )
      .then((response) => {
        this.test = response.data;
        console.log(response);
      });
  },
  methods: {
    check() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      let testData = {
        test_id: this.test.id,
        answers: Object.values(this.answers),
      };
      console.log(testData);

      axios
        .post("http://127.0.0.1:8000/pitch/check/", testData, options)
        .then((response) => {
          this.result = response.data;
          console.log(response);
        });
    },
  },
};
</script>

