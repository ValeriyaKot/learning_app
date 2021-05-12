<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Create question</h1>

    <b-form>
      <b-form-group>
        <b-form-group id="input-group-1" label="Question" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="form.text"
            type="text"
            placeholder="Enter question"
            required
          ></b-form-input>
        </b-form-group>

        <div class="container">
          <div class="row border-bottom py-2">
            <div class="col-8">Answers</div>
            <div class="col-2">Correct</div>
          </div>

          <div
            class="row border-bottom py-2"
            v-for="(item, index) in form.answers"
            :key="index"
          >
            <div class="col-8">
              {{ form.answers[index].text }}
            </div>
            <div class="col-2">
              <b-form-radio
                v-model="correctAnswerIndex"
                @change="updateCorrectAnswer"
                name="answers-radio"
                :value="index"
              ></b-form-radio>
            </div>
            <div class="col-2">
              <b-button variant="danger" @click="deleteAnswer(index)">delete</b-button>
            </div>
          </div>

          <div class="row my-2 py-2 justify-content-between">
            <div class="col-8">
              <b-form-input
                id="input-2"
                v-model="answerText"
                type="text"
                placeholder="Enter answer"
                required
              ></b-form-input>
            </div>
            <div class="col-2">
              <b-button variant="success" v-on:click="addAnswer">Add</b-button>
            </div>
          </div>
        </div>

        <div v-if="isFormValid" class="row mt-4 justify-content-center">
          <b-button v-on:click="addQuestion">Save</b-button>
        </div>
      </b-form-group>
    </b-form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        text: "",
        answers: [],
        test: this.$route.params.testId,
      },
      answerText: "",
      correctAnswerIndex: 0,
      previousCorrectAnswerIndex: 0
    }
  },
  methods: {
    addQuestion() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .post("http://127.0.0.1:8000/pitch/questions/", this.form, options)
        .then((response) => {
          console.log(response.data);
          this.$router.push("/pitch/teacher");
        })
        .catch((error) => console.log(error));
    },
    addAnswer() {
      let answer = { text: this.answerText, is_correct: false };
      this.form.answers.push(answer);
      console.log(this.form.answers);
      this.answerText = "";
      this.updateCorrectAnswer()
    },
    deleteAnswer: function (index) {
      if (!this.form.answers[index].is_correct) {
        this.form.answers.splice(index, 1)
        if (this.correctAnswerIndex > index) {
          this.previousCorrectAnswerIndex--
          this.correctAnswerIndex--
        }
      }
    },
    updateCorrectAnswer () {
      this.form.answers[this.previousCorrectAnswerIndex].is_correct = false
      this.form.answers[this.correctAnswerIndex].is_correct = true
      this.previousCorrectAnswerIndex = this.correctAnswerIndex
    }
  },
  computed: {
    isFormValid: function () {
      return this.form.answers.length >= 2 && this.form.answers.some(a => a.is_correct)
    }
  }
};
</script>