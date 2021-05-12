<template>
  <div>
    <div class="row my-2 justify-content-end">
      <div class="col-8 border-left">
        {{ test.title }}
      </div>
      <div class="col-2 text-right">
        <b-button v-b-toggle="questionsCollapseId" variant="outline-secondary"
          >Questions</b-button
        >
      </div>
      <div class="col-2 text-right">
        <b-button variant="danger" v-on:click="deleteTest">Delete</b-button>
      </div>
    </div>

    <b-collapse :id="questionsCollapseId" class="mt-2">
      <ol>
        <li
          v-for="(question, index) in test.questions"
          :index="index"
          :key="question.id"
        >
          <div class="m-2">
            {{ question.text }}

            <ul
              class="my-2"
              v-for="answer in question.answers"
              :key="answer.id"
            >
              <li>Answer: {{ answer.text }}</li>
              <li>Correct: {{ answer.is_correct }}</li>
            </ul>
          </div>
          <div class="row mt-4 justify-content-end">
            <b-button
              size="sm"
              variant="outline-danger"
              v-on:click="deleteQuestion(question.id, index)"
              >Delete question</b-button
            >
          </div>
        </li>
      </ol>
      <div class="row mt-4 mb-4 justify-content-center">
        <div class="col-3">
          <b-button
            variant="secondary"
            :href="`/pitch/courses/${courseId}/tests/${test.id}/add-questions`"
            >Add questions</b-button
          >
        </div>
      </div>
    </b-collapse>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    test: Object,
    index: Number,
    courseId: Number,
  },
  computed: {
    questionsCollapseId: function () {
      return `questions-collapse-${this.test.id}`;
    },
  },
  methods: {
    deleteQuestion: function (questionId, index) {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .delete(`http://127.0.0.1:8000/pitch/questions/${questionId}`, options)
        .then((response) => {
          if (response.status == 204) {
            this.test.questions.splice(index, 1);
          }
        });
    },
    deleteTest() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .delete(`http://127.0.0.1:8000/pitch/tests/${this.test.id}`, options)
        .then((response) => {
          console.log(response);
          if (response.status == 204) {
            this.$router.go("/pitch/teacher");
          }
        });
    },
  },
};
</script>
