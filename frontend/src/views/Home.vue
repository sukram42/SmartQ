<template>
  <div class="home">
    <div class="search_input_wrapper">
      <div class="search_input">
        <v-text-field label="Search for Restaurant">
        </v-text-field>
      </div>
    </div>
    <div id="map" ref="map">
      <maps-marker :lat="-25.344"
                   :lng="131.036"
                   :onClick="onMarkerClick"
                   :shop="{name: 'Rewe', id: 'blabla'}"
      />
    </div>
  </div>
</template>
<script>

// @ is an alias to /src
import MapsMarker from '../components/MapsMarker'

export default {
  name: 'Home',
  components: { MapsMarker },
  data: () => ({
    map: null
  }),
  methods: {
    onMarkerClick (shop) {
      this.$router.push({ path: `shopDetail/${shop.name}` })
    },
    getMap (callback) {
      /* eslint-disable */
        const that = this
        /* eslint-enable */
      function checkForMap () {
        if (that.map) {
          callback(that.map)
        } else {
          setTimeout(checkForMap, 200)
        }
      }
      checkForMap()
    }

  },
  mounted () {
    this.map = new window.google.maps.Map(this.$refs.map, {
      center: { lat: -25.344, lng: 131.036 },
      zoom: 8,
      streetViewControl: false,
      fullscreenControl: false,
      mapTypeControl: false
    })
  }
}
</script>
<style scoped lang="scss">
  .search_input_wrapper {
    position: absolute;
    width: 100vw;
    z-index: 100;
    padding: 1em;
  }

  .search_input {
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
