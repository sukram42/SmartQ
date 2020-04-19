<template>
  <div class="home">
    <div class="search_input_wrapper">
      <div class="search_input">
        <div class="headertext">Search for Shops.</div>
        <v-text-field v-model="searchString" single-line label="Search"></v-text-field>
        <div v-if="searchString.length > 0" class="info-field"> We found {{ shownShops.length>0? shownShops.length: 'no'}} result{{ shownShops.length ===1 ?'':'s'}}</div>
        <div v-if="searchString.length === 0" class="info-field"> There {{ shownShops.length > 1? 'are' : 'is'}} {{ shownShops.length>0? shownShops.length: 'no'}} store{{ shownShops.length ===1 ?'':'s'}} available</div>
      </div>
    </div>
    <div id="map" ref="map">
      <maps-marker
        v-for="shop in shownShops"
        :key="shop.id"
        :lat="shop.latitude"
        :lng="shop.longitude"
        :onClick="onMarkerClick"
        :shop="shop"
        :color="shop.waitingtime > 5?'red':'green'"
      />
    </div>
  </div>
</template>
<script>

import MapsMarker from '../components/MapsMarker'
import axios from 'axios'
import { config } from '../config/config.js'

export default {
  name: 'Home',
  components: { MapsMarker },
  data: () => ({
    map: null,
    searchString: '',
    shops: []
  }),
  computed: {
    shownShops: function () {
      return this.shops.filter((shop) => this.searchString === '' ? true : (
        shop.name.toLowerCase().includes(this.searchString.toLowerCase()) ||
        shop.category.toLowerCase().includes(this.searchString.toLowerCase())))
    }
  },
  methods: {
    onMarkerClick (shop) {
      window.localStorage.setItem('lat', this.map.getCenter().lat)
      window.localStorage.setItem('lng', this.map.getCenter().lng)
      window.localStorage.setItem('zoom', this.map.getZoom())
      this.$router.push({ path: `shopDetail/${shop.id}` })
    },
    /**
     * Method to enable children (Markers and co) to get access to the map.
     * @param callback
     */
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
    },
    loadShops: async () => {
      return axios.get(`${config.baseApi}/shops`)
    }
  },
  async mounted () {
    const lat = window.localStorage.getItem('lat')
    const lng = window.localStorage.getItem('lng')
    const zoom = window.localStorage.getItem('zoom')

    // Map configurations
    this.map = new window.google.maps.Map(this.$refs.map, {
      center: {
        lat: parseFloat(lat) || 48.137357,
        lng: parseFloat(lng) || 11.575202
      },
      zoom: parseFloat(zoom) || 15,
      streetViewControl: false,
      fullscreenControl: false,
      mapTypeControl: false
    })

    this.shops = (await this.loadShops()).data
  }
}
</script>
<style scoped lang="scss">
  .search_input_wrapper {
    position: absolute;
    width: 100vw;
    z-index: 100;
    padding: 0.5em;
  }

  .search_input {
    border-radius: 5px;
    z-index: 1000;
    background-color: white;
    padding:1em
  }
  .info-field {
    font-size: 0.8em;
  }
  #map {
    height: calc(100vh - 50px);
    width: 100vw;
  }
  .headertext {
    font-weight: bold;
    font-size: 1.5em;
    color: black;
  }
</style>
