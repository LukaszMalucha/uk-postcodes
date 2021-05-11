import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import StandardValidation from "./views/StandardValidation.vue";
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
      path: "*",
      name: "page-not-found",
      component: NotFound,
    },
  ]
})
