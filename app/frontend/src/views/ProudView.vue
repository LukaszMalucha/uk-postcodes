<template>
<div id="page-index">
    <div v-if="!isLoggedIn()"  class="dashboard-cards">
        <NoPermissionComponent/>
    </div>
    <div v-if="getUsername()" class="dashboard-cards">
    <div class="row row-search">
      <br><br>
      <div class="row row-proud left-align">
        I am so proud of my wife Agata. Over a year ago, I convinced her to start learning to code in Python. New beginnings are never easy, but she stayed on the path, building several family-useful applications along the way. Earlier this year, she decided to get her Python diploma at UCD and she is currently building her final project. There is no greater reward than seeing her seriously engaged and focused on this task.
      </div>
      <br><br>
      <div class="row row-proud left-align">
        <div class="col s4 m4 l3  plain-element">
          <img alt="Avatar" class="avatar" src="https://avatars.githubusercontent.com/u/42006092?v=4">
        </div>
        <div class="col s8 m8 l8  plain-element">
            <a href="https://github.com/agatamalucha/UCDPA_agatamalucha" target="_blank">UCDPA Covid-19 Project </a>
        </div>
      </div>
    </div>
  </div>
</div>
</template>


<script>
import { mapGetters } from "vuex";
import NoPermissionComponent from "@/components/NoPermissionComponent.vue"

export default {
  name: "ProudView",
  components: {
    NoPermissionComponent,
  },
  data() {
    return {
    }
  },
  methods: {
    ...mapGetters([ "getUsername", "isLoggedIn"]),
  },
  computed: {

  },
  mounted() {
  },
  created() {
    document.title = "What I'm Proud Of";

  }
}

</script>