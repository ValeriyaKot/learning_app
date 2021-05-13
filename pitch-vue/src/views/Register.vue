<template>
  <div class="container">
    <h1 class="text-center mt-4 mb-4">Register</h1>

    <b-form>
      <b-form-group id="input-group-1" label="Username*" label-for="input-1">
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

      <b-form-group id="input-group-2" label="First name" label-for="input-2">
        <b-form-input
          id="input-2"
          v-model="form.first_name"
          type="text"
          placeholder="Enter first name"
          trim
        ></b-form-input>
      </b-form-group>

      <b-form-group id="input-group-3" label="Last name" label-for="input-3">
        <b-form-input
          id="input-3"
          v-model="form.last_name"
          type="text"
          placeholder="Enter last name"
          trim
        ></b-form-input>
      </b-form-group>

      <b-form-group
        id="input-group-4"
        label="Password*"
        label-for="input-4"
        description="Your password must be 8-20 characters long, contain letters and
            numbers, and must not contain spaces, special characters, or emoji."
      >
        <b-form-input
          v-model="form.password"
          type="password"
          id="input-4"
          placeholder="Enter password"
          required
          trim
        ></b-form-input>

        <b-form-text
          v-for="(message, index) in errorMessages.password"
          :key="index"
          :id="`input-4-error-${index}`"
        >
          <span class="error-message">{{ message }}</span>
        </b-form-text>
      </b-form-group>

      <b-form-group
        id="input-group-5"
        label="Email address*"
        label-for="input-5"
        description="We'll never share your email with anyone else."
      >
        <b-form-input
          id="input-5"
          v-model="form.email"
          type="email"
          placeholder="Enter email"
          required
          trim
        ></b-form-input>

        <b-form-text
          v-for="(message, index) in errorMessages.email"
          :key="index"
          :id="`input-5-error-${index}`"
        >
          <span class="error-message">{{ message }}</span>
        </b-form-text>
      </b-form-group>

      <b-form-group id="input-group-6" label="Role*" label-for="input-6">
        <b-form-select
          id="input-6"
          v-model="form.profile.role"
          :options="roles"
          required
        ></b-form-select>

        <b-form-text
          v-for="(message, index) in errorMessages.role"
          :key="index"
          :id="`input-6-error-${index}`"
        >
          <span class="error-message">{{ message }}</span>
        </b-form-text>
      </b-form-group>

      <b-form-group id="input-group-7" label="Birthday" label-for="input-7">
        <b-form-datepicker
          id="input-7"
          v-model="form.profile.birthday"
          type="date"
          placeholder="Enter birthday"
        ></b-form-datepicker>

        <b-form-text
          v-for="(message, index) in errorMessages.birthday"
          :key="index"
          :id="`input-7-error-${index}`"
        >
          <span class="error-message">{{ message }}</span>
        </b-form-text>
      </b-form-group>
    </b-form>

    <p>* - required</p>
    <div class="row mt-4 justify-content-center">
      <b-button v-on:click.prevent="register" type="submit" variant="secondary"
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
        email: "",
        username: "",
        first_name: "",
        last_name: "",
        password: "",
        profile: {
          birthday: "",
          role: null,
        },
      },
      errorMessages: {},
      roles: [{ text: "Select One", value: null }, "student", "teacher"],
    };
  },
  methods: {
    register() {
      console.log(this.form);
      axios
        .post("http://127.0.0.1:8000/pitch/auth/register", this.form)
        .then((response) => {
          console.log(response.data);
          this.$router.push("/pitch/login");
        })
        .catch((error) => {
          if (error.response && error.response.status == 400) {
            console.log(error.response);
            this.errorMessages = {
              role: error.response.data.profile == null ? null : error.response.data.profile.role,
              birthday: error.response.data.profile == null ? null : error.response.data.profile.birthday,
              ...error.response.data
            }
          }
        });
    },
  },
};
</script>

<style>
.error-message {
  color: red;
}
</style>