<template>
  <div class="home">
    <div class="search_input_wrapper">
      <div class="search_input">
        <v-text-field v-model="searchString" label="Search" clearable>
        </v-text-field>
        <div v-if="searchString.length > 0" class="info-field"> we found {{ shownShops.length>0? shownShops.length: 'no'}} result{{ shownShops.length ===1 ?'':'s'}}</div>
        <div v-if="searchString.length === 0" class="info-field"> there {{ shownShops.length > 1? 'are' : 'is'}} {{ shownShops.length>0? shownShops.length: 'no'}} store{{ shownShops.length ===1 ?'':'s'}} available</div>
      </div>
    </div>
    <div id="map" ref="map">
      <maps-marker
        v-for="shop in shownShops"
        :key="shop.id"
        :lat="shop.lat"
        :lng="shop.lat"
        :onClick="onMarkerClick"
        :shop="shop"
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
    shops: [{
      lat: 10,
      lon: 10,
      id: 'jfsdkfj',
      name: 'Rewestore',
      category: 'grocery'
    }]
  }),
  computed: {
    shownShops: function () {
      return this.shops.filter((shop) => this.searchString === '' ? true : (
        shop.name.includes(this.searchString) ||
        shop.category.includes(this.searchString)))
    }
  },
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
    },
    loadShops: async () => {
      return axios.get(`${config.baseApi}/shops`)
    }
  },
  async mounted () {
    this.map = new window.google.maps.Map(this.$refs.map, {
      center: { lat: 10, lng: 10 },
      zoom: 8,
      streetViewControl: false,
      fullscreenControl: false,
      mapTypeControl: false
    })

    this.shops = await this.loadShops()
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
  .info-field {
    font-size: 0.8em;
    padding: -3% 0;
  }
  #map {
    height: calc(100vh - 50px);
    width: 100vw;
  }
</style>
