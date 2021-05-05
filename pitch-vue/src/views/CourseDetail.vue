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
        <p v-for="module in course.modules" :key="module.id">
            <ul>
                <li>{{ module.title }}</li>
            </ul>
        </p>
      </b-card-text>
      <b-button variant="outline-secondary" :href="`/pitch/courses/${course.id}`">learn more</b-button>
      <b-button variant="secondary" href="#">enroll</b-button>
    </b-card>
  </div>
</template>

<script>
import axios from 'axios'
export default {
    name: 'CourseDetail',
    data() {
        return {
            course: {}
        }
    },
//   components: {
//     CourseItem
//   },
  mounted() {
    axios
        .get(`http://127.0.0.1:8000/pitch/courses/${this.$route.params.id}`)
        .then(response => {
            this.course = response.data
            console.log(response)
        })
        

    } 
  }
    
</script>
