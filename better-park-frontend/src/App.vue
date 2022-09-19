<template>
  <v-app>
    <v-app-bar app color="#0068c0" dark>
      <div class="d-flex align-center mx-10" >
        <v-img alt="Vuetify Logo" class="shrink" contain :src="require('./assets/BetterPark_Logo.webp')"
          transition="scale-transition" />
      </div>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
      <notifications position="bottom left"/>
    </v-main>
  </v-app>
</template>

<script>
  export default {
    name: 'App',

    components: {},

    data: () => ({}),
  };
</script>

<style>
@import url('https://fonts.googleapis.com/css?family=Lato:300,400,700');

html, body {
  font-family: 'Lato', sans-serif;
}

#app {
  font-family: 'Lato', sans-serif;
}

h1{
  font-size: 35px !important;
  color: #0068c0;
}

P{
  font-size: 20px !important;
  color:black !important;
}

.input-field{
  font-size: 32px !important;
}

.input-field input{
  text-align: center !important;
  color:#595959 !important;
}

.details{
  color:black !important;
}

.input input{
    color:#595959 !important;
}
</style>