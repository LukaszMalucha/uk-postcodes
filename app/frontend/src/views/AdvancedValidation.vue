<template>
<div id="page-index">
  <div class="dashboard-cards">
    <div class="row row-search">
      <div class="row plain-element left-align">
        <div class="search-container">
          <div class="row searchbox-wrapper">
            <form @submit.prevent="submitQuery">
              <input v-model="searchQuery" class="form-control" id="searchbox" type="text"
                     placeholder="Validate Postcode"
                     aria-label="Validate Postcode">
              <button class="btn-transparent" type="submit"><i class="fas fa-search search-icon"></i></button>
            </form>
          </div>
        </div>
      </div>
      <div class="row row-error text-center">
        <p class="error" id="formError"  v-if="getFormError()">{{ getFormError() }}</p>
        <p class="error" v-else></p>
      </div>
      <br>
      <br>
      <div id="result" class="row plain-element">
        <div v-if="getResult()" class="row row-result text-center">
          <p class="invalid" v-if="getResult().result == 'Invalid'"> Postcode "{{ getPostcode() }}" is Invalid</p>
          <table  v-if="getResult().postcode" style="width:100%">
            <tr>
              <td>Postcode:</td>
              <td>{{ getPostcode() }}</td>
            </tr>
            <tr>
              <td>County:</td>
              <td>{{ getResult().county }}</td>
            </tr>
            <tr>
              <td>District:</td>
              <td>{{ getResult().district }}</td>
            </tr>
            <tr>
              <td>Ward:</td>
              <td>{{ getResult().ward }}</td>
            </tr>
            <tr>
              <td>Constituency:</td>
              <td>{{ getResult().constituency }}</td>
            </tr>
          </table>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>

import { mapGetters, mapActions } from "vuex";


export default {
  name: "StandardValidation",
  data() {
    return {
      search: "",
      searchQuery: null,
    }
  },
  methods: {
    ...mapGetters(["getFormError", "getResult", "getPostcode"]),
    ...mapActions(["fetchAdvancedValidation","performSetFormError"]),
    submitQuery() {
      this.search = "";
      document.getElementById("result").style.display = "block";
      this.fetchAdvancedValidation({"postcode": this.searchQuery})
    },
  },
  computed: {

  },
  created() {
    document.title = "Advanced Validation";
    this.performSetFormError(null);
  }
}

</script>