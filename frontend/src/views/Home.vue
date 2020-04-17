<template>
  <div class="home">
    <div class="search_input_wrapper">
      <div class="search_input">
        <v-text-field label="Search for Restaurant">
        </v-text-field>
      </div>
    </div>
    <div id="map" ref="map">
    </div>
  </div>
</template>
<script>

// @ is an alias to /src
export default {
  name: 'Home',
  components: {},

  data: () => ({
    map: null
  }),

  mounted () {
    this.map = new window.google.maps.Map(this.$refs.map, {
      center: { lat: -34.397, lng: 150.644 },
      zoom: 8,
      streetViewControl: false,
      fullscreenControl: false,
      mapTypeControl: false
    })
  }
}
</script>
<style scoped lang="scss">
  .search_input_wrapper{
    position: absolute;
    width: 100vw;
    z-index: 100;
    padding: 1em;
  }
  .search_input{
    border-radius: 5px;
    z-index: 1000;
    background-color: white;

    padding: 1% 4% 0 4%;

  }
  #map {
    height: calc(100vh - 50px);
    width: 100vw;
  }
</style>
