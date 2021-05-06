 <template>
    <div class="container mb-3">
        <h1>Test.title</h1>
        <ul>
            <li>
                <p>Question</p>
            <b-form-checkbox
      id="checkbox-1"
      name="checkbox-1"
      value="question"
    >
    Answer
    </b-form-checkbox>
    <div>Your answer: <strong>Answer</strong></div>
            </li>
        </ul>

    <h3>Test result: </h3>
    </div>
 </template>

<script>
import axios from 'axios'
export default {
    name: 'Test',
    data() {
        return {
            test: {}
        }
    },
  mounted() {
    axios
        .get(`http://127.0.0.1:8000/pitch/tests/${this.$route.params.id}`)
        .then(response => {
            this.test = response.data
            console.log(response)
        })
        

    } 
  }
</script>

