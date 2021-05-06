<template>
    <div class="container mb-3">
        <h1 class="card-title">
          {{ course.title }}
        </h1>
        <p class="card-text">
          {{ course.description }}
        </p>
        <h3>Modules</h3>
        <p v-for="module in course.modules" :key="module.id">
            <ul>
                <li>
                    <h4>{{ module.title }}</h4>
                    <div v-for="material in module.materials" :key="material.id">
                        <p>{{ material.text }}</p>
                        <b-button size="sm" variant="secondary" href="#">add material</b-button>
                        <b-button size="sm" variant="outline-secondary" href="#">edit module</b-button>
                    </div>
                </li>
            </ul>
        </p>
        <h3>Tests</h3>
        <p v-for="test in course.tests" :key="test.id">
            <ul>
              <li>{{ test.title }}</li>
                <b-button size="sm" svariant="secondary" :href="`/pitch/tests/${test.id}`">run</b-button>
                <b-button size="sm" svariant="secondary" href="#">edit</b-button>
            </ul>
        </p>
        <b-button svariant="secondary" href="#">enroll</b-button>
        <b-button svariant="secondary" href="#">add module</b-button>
        <b-button svariant="secondary" href="#">add test</b-button>
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
