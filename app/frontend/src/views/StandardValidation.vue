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
      <div class="row row-result text-center">
        <p  id="result"  v-if="getResult()">{{ getResult() }}</p>
        <p v-else></p>
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
    ...mapGetters(["getFormError", "getResult"]),
    ...mapActions(["fetchStandardValidation","performSetFormError"]),
    submitQuery() {
      this.search = "";
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