<template>
  <div class="container">
    <div class="row my-2 justify-content-end">
      <div class="col-8 border-left">
        {{ test.title }}
      </div>
      <div class="col-4 text-right">
        <b-button
          variant="secondary"
          :href="`/pitch/courses/${courseId}/tests/${test.id}`"
          >Check</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: {
    test: Object,
    index: Number,
    courseId: Number,
  },
};
</script>