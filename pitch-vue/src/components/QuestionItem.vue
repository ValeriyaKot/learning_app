<template>
  <div>
    <ul>
      <li>
        {{ question.text }}
        <b-form-radio
          v-model="selected"
          v-for="answer in question.answers"
          :key="answer.id"
          :name="question.text"
          :value="answer.text"
          v-on:change="updateAnswer"
        >{{ answer.text }}</b-form-radio>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  props: {
    question: Object,
    answers: Object,
  },
  data() {
    return {
      selected: '',
    };
  },
  methods: {
    updateAnswer() {
        let selectedAnswer = {
            "question_id": this.question.id,
            "answer": this.selected
        }
        this.answers[this.question.id] = selectedAnswer
        console.log(this.answers)
    }
  }
};
</script>

<style>
</style>