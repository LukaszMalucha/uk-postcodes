<template>
<div id="page-index">
  <div class="dashboard-cards">
    <div class="row row-search">
      <div v-if="getNumbers()" class="row row-numbers">
        <div v-for="(element, index) in getNumbers()" class="col s4 m2 l1 col-link" :key="index">
          <div class="card number-card">
            <span v-if="element == 'Three'" class="font-yellow">{{ element }}</span>
            <span v-else-if="element == 'Five'" class="font-green">{{ element }}</span>
            <span v-else-if="element == 'ThreeFive'" class="font-red">{{ element }}</span>
            <span v-else>{{ element }}</span>
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