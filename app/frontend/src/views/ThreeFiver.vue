<template>
<div id="page-index">
  <div class="dashboard-cards">
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


export default {
  name: "ThreeFiver",
  components: {
  },
  data() {
    return {
    }
  },
  methods: {
    ...mapGetters(["getNumbers"]),
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