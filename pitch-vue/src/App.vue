<template>
  <div id="app">
    <Nav :isLoggedIn="isLoggedIn"/>
    <router-view />
  </div>
</template>

<script>
    import Nav from './components/Nav.vue';
    export default {
      data () {
        return {
          isLoggedIn: localStorage.getItem("token") !== null ? true : false
        }
      },
      components: {Nav},
      methods: {
        logout () {
          alert('Logging out')
        }
      }
    }
</script>

<style>
</style>
