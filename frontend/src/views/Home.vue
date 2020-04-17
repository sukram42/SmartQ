<template>
  <div class="home">

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
  #map {
    height: calc(100vh - 50px);
    width: 100%;
  }
</style>
