<template>
    <footer class="bg-dark text-center text-white">
    <div class="text-center p-3" style="background-color: rgba(0, 0, 0, 0.2);">
        © 2021 Pitch:
    </div>
    </footer>
</template>

<script>
  export default {
    data() {
      return {
        year: new Date().getFullYear()
      };
    }
  };
</script>
<style scoped>
  /* .footer {
    height: 80px;
	margin-top: 0px
  } */
</style>