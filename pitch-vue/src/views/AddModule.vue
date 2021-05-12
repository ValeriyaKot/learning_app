<template>
  <div class="container">
    <h1 class="text-center mb-4 mt-4">Add module</h1>

    <b-form>
      <b-form-group>
        <b-form-group id="input-group-1" label="Title" label-for="input-1">
          <b-form-input
            id="input-1"
            v-model="form.title"
            type="text"
            placeholder="Enter module title"
            required
          ></b-form-input>
        </b-form-group>

        <div class="container">
          <div class="row border-bottom py-2">
            <div class="col-8">Materials</div>
          </div>

          <div
            class="row border-bottom py-2"
            v-for="(item, index) in form.materials"
            :key="index"
          >
            <div class="col-8">
              {{ form.materials[index].text }}
            </div>
            <div class="col-2">
              <b-button variant="danger" @click="deleteMaterial(index)"
                >Delete</b-button
              >
            </div>
          </div>

          <div class="row my-2 py-2 justify-content-between">
            <div class="col-8">
              <b-form-group id="input-group-3" label-for="input-3">
                <b-form-input
                  id="input-3"
                  v-model="material"
                  type="text"
                  placeholder="Enter material"
                  required
                ></b-form-input>
              </b-form-group>

              <b-button v-on:click="addMaterial" variant="success"
                >Add</b-button
              >
            </div>
          </div>
        </div>
      </b-form-group>
    </b-form>

    <div class="row mt-4 mb-4 justify-content-center">
      <div class="row mt-4 justify-content-center">
        <b-button v-if="isFormValid" v-on:click="addModule" variant="secondary"
          >Save</b-button
        >
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      form: {
        title: "",
        materials: [],
        course: this.$route.params.id,
      },
      material: "",
    };
  },
  methods: {
    addModule() {
      let token = JSON.parse(localStorage.getItem("token"))["access"];
      let options = {
        headers: { Authorization: "Bearer " + token },
      };
      console.log(this.form),
        axios
          .post("http://127.0.0.1:8000/pitch/modules/", this.form, options)
          .then((response) => {
            console.log(response.data);
            this.$router.push("/pitch/teacher");
          })
          .catch((error) => console.log(error));
    },
    addMaterial() {
      let material = { text: this.material };
      this.form.materials.push(material);
      console.log(this.form.materials);
      this.material = "";
    },
    deleteMaterial: function (index) {
      this.form.materials.splice(index, 1);
    },
  },
  computed: {
    isFormValid: function () {
      return this.form.materials.length >= 1;
    },
  },
};
</script>