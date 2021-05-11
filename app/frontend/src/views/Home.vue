<template>
  <div id="page-index">
    <div class="dashboard-cards">

      <div class="row row-title">
        <div class="page-title-container">
          <h4 class="page-title underline-blue">
            Postcode Validation Portal
          </h4>
        </div>
      </div>
      <div class="row row-cards">
        <div class="col s12 m3 l3 plain-element"></div>
        <div class="col s12 m3 l3 plain-element">
          <router-link :to="{name: 'standard-validation'}">
            <div class="card card-menu">
              <div class="card-image">
                <img class="img-menu" src="/static/img/pin.png" alt="pin1"/>
              </div>
              <div class="card-content">
                <span class="card-title">Standard Validation</span>
              </div>
            </div>
          </router-link>
        </div>
        <div class="col s12 m3 l3 plain-element">
          <router-link :to="{name: 'advanced-validation'}">
            <div class="card card-menu">
              <div class="card-image">
                <img class="img-menu" src="/static/img/pin_2.png" alt="pin2"/>
              </div>
              <div class="card-content">
                <span class="card-title">Advanced Validation</span>
              </div>
            </div>
          </router-link>
        </div>
        <div class="col s12 m3 l3 plain-element">
          <router-link :to="{name: 'advanced-validation'}">
            <div class="card card-menu">
              <div class="card-image">
                <img class="img-menu" src="/static/img/35.png" alt="35"/>
              </div>
              <div class="card-content">
                <span class="card-title">ThreeFiver</span>
              </div>
            </div>
          </router-link>

        </div>
      </div>

    </div>
  </div>
</template>


<script>

export default {
  name: "Home",
  data() {
    return {

    }
  },
  methods: {

  },
  computed: {

  },
  created() {

    document.title = "UK Postcodes";
  }
}

</script>