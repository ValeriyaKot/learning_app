<template>
  <div class="container mb-3">
    <b-card body-class="text-center">
      <b-card-text>
        <h3 class="card-title">
          {{ course.title }}
        </h3>
        <p class="card-text">
          {{ course.description }}
        </p>
      </b-card-text>
      <b-button variant="outline-secondary" :href="`/pitch/courses/${course.id}`">learn more</b-button>
      <b-button variant="secondary" href="#">enroll</b-button>
    </b-card>
  </div>
</template>

<script>
export default {
  props: {
      course: Object,
      index: Number,
      title: String,
  },
  components: {
  }
}
</script>

<style>
</style>