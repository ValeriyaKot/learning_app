<template>
  <div class="container">
    <div class="row py-2 border-top">
      <div class="col-8">
        {{ result.test }}
      </div>
      <div class="col-2">
        Result: {{ result.result }}
      </div>        
      <div class="col-2">
        <b-button v-b-toggle="collapseId" variant="outline-secondary">Questions</b-button>
      </div>

      <b-collapse :id="collapseId" class="mt-2">
        <ol>
          <li v-for="studentAnswer in result.student_answers"
            :key="studentAnswer.id"
          >
            <div class="my-2">
              {{ studentAnswer.question }}
              <ul class="my-2" v-if="studentAnswer.is_correct">
                <li class="correct-answer">Your answer: {{ studentAnswer.answer }}</li>
              </ul>
              <ul v-else class="my-2">
                <li class="answer">Your answer: {{ studentAnswer.answer }}</li>
                <li class="correct-answer">Correct answer: {{ studentAnswer.correct_answer }}</li>
              </ul>
            </div>
          </li>
        </ol>
      </b-collapse>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    result: Object,
    index: Number
  },
  computed: {
    collapseId: function () {
      return `collapse-${this.index}`
    }
  }
}
</script>

<style>
  .correct-answer {
    color: green;
  }
  .answer{
    color: red;
  }

</style>
