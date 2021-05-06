<template>
  <div id="app">
    <Nav />
    <router-view />
    <span v-if="isLoggedIn"> | <a @click="logout">Logout</a></span>
    <!-- <Footer /> -->
  </div>
</template>

<script>
    import Nav from './components/Nav.vue';
    // import Footer from './components/Footer.vue';
    export default {
        components: {Nav}
    }
</script>

<style>
/* #app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: auto;
  padding-bottom: 0px;
} */
</style>
