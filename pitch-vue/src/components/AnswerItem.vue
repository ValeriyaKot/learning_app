<template>
  <div>
    <b-form-radio
      :aria-describedby="ariaDescribedby"
      name="some-radios"
      >{{ answer.text }}</b-form-radio
    >
  </div>
</template>

<script>
export default {
  props: {
    answer: Object,
  }
};
</script>
