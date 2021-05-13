<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Change password</h1>

    <b-form>
      <b-form-group>
        <b-form-group label="Current password" label-for="input-1">
          <b-form-input
            v-model="form.current_password"
            type="password"
            id="input-1"
            placeholder="Enter current password"
          ></b-form-input>

          <b-form-text
            v-for="(message, index) in errorMessages.current_password"
            :key="index"
            :id="`input-1-error-${index}`"
          >
            <span class="error-message">{{ message }}</span>
          </b-form-text>
        </b-form-group>

        <b-form-group
          label="New password"
          label-for="input-2"
          description="Your password must be 8-20 characters long, contain letters andnumbers, and must not contain spaces, special characters, or emoji."
        >
          <b-form-input
            type="password"
            v-model="form.new_password"
            id="input-2"
            placeholder="Enter new password"
          ></b-form-input>

          <b-form-text
            v-for="(message, index) in errorMessages.new_password"
            :key="index"
            :id="`input-2-error-${index}`"
          >
            <span class="error-message">{{ message }}</span>
          </b-form-text>
        </b-form-group>
      </b-form-group>
    </b-form>

    <div class="row mt-4 justify-content-center">
      <b-button v-on:click="passwordChange" type="submit" variant="secondary"
        >Save</b-button
      >
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        current_password: "",
        new_password: "",
      },
      errorMessages: {},
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      JSON.stringify(this.form);
    },
    passwordChange() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      axios
        .post(
          "http://127.0.0.1:8000/pitch/auth/password_change",
          this.form,
          options
        )
        .then((response) => {
          console.log(response.data);
          this.$router.push("/pitch/login");
        })
        .catch((error) => {
          if (error.response && error.response.status == 400) {
            console.log(error.response);
            this.errorMessages = error.response.data;
          }
        });
    },
  },
};
</script>
