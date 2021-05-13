<template>
  <div>
    <div class="container-fluid">
      <div>
        <h1 class="mt-4">Profile</h1>
        <h5>Full name: {{ profile.first_name }} {{ profile.last_name }}</h5>
        <h5>Birthday: {{ profile.birthday }}</h5>
        <h5>Role: {{ profile.role }}</h5>
        <b-link href="/pitch/change-password" class="card-link"
          >Change password</b-link>
      </div>
    </div>
    <div class="container-fluid">
      <h1 class="mt-4">Your progress</h1>
      <ul>
        <li>
          <b-link href="/pitch/profile/tests-results">Tests results</b-link>
        </li>
        <li>
          <b-link href="/pitch/profile/courses">Your courses</b-link>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Profile",
  data() {
    return {
      profile: {},
    };
  },

  mounted() {
    let token = JSON.parse(localStorage.getItem("token"))["access"];
    let options = {
      headers: { Authorization: "Bearer " + token },
    };

    axios
      .get("http://127.0.0.1:8000/pitch/profile", options)
      .then((response) => (this.profile = response.data[0]));
  },
};
</script>