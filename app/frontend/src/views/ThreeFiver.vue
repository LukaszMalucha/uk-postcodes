<template>
<div id="page-index">
    <div v-if="!isLoggedIn()"  class="dashboard-cards">
        <NoPermissionComponent/>
    </div>
    <div v-if="getUsername()" class="dashboard-cards">
    <div class="row row-search">
      <div v-if="getNumbers()" class="row row-numbers">
        <div v-for="(element, index) in getNumbers()" class="col s4 m2 l1 col-link" :key="index">
          <div class="card number-card">
            <span>{{ element }}</span>
          </div>
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
  name: "ThreeFiver",
  components: {
    NoPermissionComponent,
  },
  data() {
    return {
    }
  },
  methods: {
    ...mapGetters(["getNumbers", "getUsername", "isLoggedIn"]),
    ...mapActions(["fetchThreeFiver"]),
  },
  computed: {

  },
  mounted() {
  },
  created() {
    document.title = "ThreeFiver";
    this.fetchThreeFiver();
  }
}

</script>