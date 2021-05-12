<template>
  <div id="navbar">
    <b-navbar toggleable="lg" type="dark" variant="dark">
      <b-navbar-brand>Pitch</b-navbar-brand>
      <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

      <b-collapse id="nav-collapse" is-nav>
        <b-navbar-nav>
          <b-nav-item href="/pitch">Home</b-nav-item>
        </b-navbar-nav>
        <b-navbar-nav>
          <b-nav-item href="/pitch/courses">Courses</b-nav-item>
        </b-navbar-nav>

        <b-navbar-nav class="ml-auto">
          <b-nav-item-dropdown right>
            <template #button-content>
              <em>User</em>
            </template>
            <b-dropdown-item v-if="isLoggedIn" href="/pitch/profile">Profile</b-dropdown-item>
            <b-dropdown-item v-if="isTeacher" href="/pitch/teacher">Teacher's room</b-dropdown-item>
            <b-dropdown-item v-if="isLoggedIn" v-on:click="logout">Log out</b-dropdown-item>
            <b-dropdown-item v-else href="/pitch/login">Log in</b-dropdown-item>
          </b-nav-item-dropdown>
        </b-navbar-nav>
      </b-collapse>
    </b-navbar>
  </div>
</template>

<script>
export default {
  props: {
    isLoggedIn: Boolean,
  },
  methods: {
    logout() {
      localStorage.clear()
      this.isLoggedIn = false
      this.isTeacher = false
      this.$router.push('/pitch/login')
    },
  },
  computed: {
      isTeacher: function () {
        let role = localStorage.getItem("role");
        return role === 'teacher'
    },
    },
};
</script>

<style>
</style>
