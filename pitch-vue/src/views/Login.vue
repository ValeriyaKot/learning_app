<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Log in</h1>

    <b-form>
      <b-form-group>
        <b-form-group id="input-group-1" label="Username" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="form.username"
            type="text"
            placeholder="Enter username"
            required
            trim
          ></b-form-input>

          <b-form-text
            v-for="(message, index) in errorMessages.username"
            :key="index"
            :id="`input-1-error-${index}`"
          >
            <span class="error-message">{{ message }}</span>
          </b-form-text>
        </b-form-group>

        <b-form-group
          id="input-group-2"
          label="Password"
          label-for="input-2"
          description="Your password must be 8-20 characters long, contain letters andnumbers, and must not contain spaces, special characters, or emoji.">
          <b-form-input
            v-model="form.password"
            type="password"
            id="input-2"
            placeholder="Enter password"
            trim
          ></b-form-input>

          <b-form-text
            v-for="(message, index) in errorMessages.password"
            :key="index"
            :id="`input-2-error-${index}`"
          >
            <span class="error-message">{{ message }}</span>
          </b-form-text>
        </b-form-group>
      </b-form-group>
    </b-form>

    <div class="row mt-4 justify-content-center">
      <b-link href="/pitch/register" class="card-link">Register</b-link>
    </div>

    <div class="row mt-4 justify-content-center">
      <b-button v-on:click.prevent="login" variant="secondary">Submit</b-button>
    </div>

    <b-modal id="error-modal" hide-header hide-footer>
      <div class="d-block text-center">
        <h4 class="mb-4">Error</h4>
        <div v-for="(message, index) in this.errorMessages" :key="index">{{ message }}</div>
      </div>
      <b-button class="mt-4" block @click="$bvModal.hide('error-modal')">Ok</b-button>
    </b-modal>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: {
    isLoggedIn: Boolean,
  },
  data() {
    return {
      form: {
        username: "",
        password: "",
      },
      errorMessages: {},
    };
  },
  methods: {
    login() {
      axios
        .post("http://127.0.0.1:8000/pitch/auth/login", this.form)
        .then((response) => {
          console.log(response.data);
          localStorage.setItem(
            "token",
            JSON.stringify(response.data["auth_token"])
          );
          localStorage.setItem("id", response.data["id"]);
          localStorage.setItem("username", response.data["username"]);
          localStorage.setItem("email", response.data["email"]);
          localStorage.setItem("profileId", response.data["profile"]["id"]);
          localStorage.setItem("role", response.data["profile"]["role"]);
          this.isLoggedIn = true;
          this.$router.push("/pitch");
        })
        .catch((error) => {
          if (error.response && error.response.status == 400) {
            console.log(error.response);
            this.errorMessages = error.response.data

            if (error.response.data instanceof Array) {
              this.$bvModal.show('error-modal')
            }
          }
        });
    },
  },
};
</script>
