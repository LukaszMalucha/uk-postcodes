import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import StandardValidation from "./views/StandardValidation.vue";
import AdvancedValidation from "./views/AdvancedValidation.vue";
import ThreeFiver from "./views/ThreeFiver.vue";
import NotFound from "./views/NotFound.vue";

Vue.use(Router)

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "home",
      component: Home
    },
    {
      path: "/standard",
      name: "standard-validation",
      component: StandardValidation,
    },
    {
      path: "/advanced",
      name: "advanced-validation",
      component: AdvancedValidation,
    },
    {
      path: "/threefiver",
      name: "threefiver",
      component: ThreeFiver,
    },
    {
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
