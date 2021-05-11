<template>
<div id="page-index">
    <div v-if="!isLoggedIn()"  class="dashboard-cards">
        <NoPermissionComponent/>
    </div>
    <div v-if="getUsername()" class="dashboard-cards">
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
          <p class="valid" v-if="getResult() == 'Valid'"> Postcode "{{ getPostcode() }}" is Valid</p>
          <p class="invalid" v-else> Postcode "{{ getPostcode() }}" is Invalid</p>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>

import { mapGetters, mapActions } from "vuex";
import NoPermissionComponent from "@/components/NoPermissionComponent.vue"

export default {
  name: "StandardValidation",
  components: {
    NoPermissionComponent,
  },
  data() {
    return {
      search: "",
      searchQuery: null,
    }
  },
  methods: {
    ...mapGetters(["getFormError", "getResult", "getPostcode", "getUsername", "isLoggedIn"]),
    ...mapActions(["fetchStandardValidation","performSetFormError"]),
    submitQuery() {
      this.search = "";
      document.getElementById("result").style.display = "block";
      this.fetchStandardValidation({"postcode": this.searchQuery})
    },
  },
  computed: {

  },
  created() {

    document.title = "Standard Validation";
    this.performSetFormError(null);
  }
}

</script>