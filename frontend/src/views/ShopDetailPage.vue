<template>
  <div class="infos">
    <div class="image">
      <v-btn class="back-btn" color="#02FF04" v-on:click="()=>$router.go(-1)"> Go back</v-btn>
    </div>
    <div class="store-info">
      <div class="store">{{shop.category}}</div>
      <div class="name">{{ shop.name }}</div>
      <div class="address">
        <div>{{ shop.address.split(',')[0] }}</div>
        <div class="divider">|</div>
        <div> {{ shop.address.split(',')[1] }}</div>
      </div>
    </div>
    <div class="shareinfos">
      <img alt="show on map" src="../assets/iconmonstr-map-8-240.png" v-on:click="()=>openInMaps()">
      <img alt="show website" src="../assets/iconmonstr-networking-6-240.png" v-on:click="()=>openWebsite()">
    </div>
    <div class="waiting">
      <div class="waiting-number"> 999 </div>
      <div class="waiting-label"> Waiting</div>
    </div>
    <div class="chart">
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { config } from '../config/config.js'

export default {
  name: 'ShopDetailPage',
  data: () => ({
    shop: {
      id: 1,
      name: 'Penny Schwabing',
      category: 'groceries',
      address: 'Musterweg 15, 80807 München',
      latitude: 48.2,
      longitude: 11.5,
      storespace: 800,
      maxcapacity: 50,
      capacity: 92.5,
      waitingtime: 5,
      lastupdate: {},
      website: 'www.google.de'
    }
  }),
  methods: {
    openInMaps: () => {
      window.open(`http://www.google.com/maps/place/${this.shop.lat},${this.shop.lng}`)
    },
    openWebsite: () => {
      const website = this.shop.website
      window.open(`${website}`)
    },
    loadShopInfo: async function () {
      return axios.get(`${config.baseApi}/shopInfo/${this.$route.params.shopID}`)
    }
  },
  async mounted () {
    this.shop = await this.loadShopInfo()
  }
}
</script>

<style scoped>
  img{
    height: 3em;
  }
  img:hover{
    : darkgreen;
  }
  .infos{
    color: black;
    width: 100vw;
    max-width: 100%;
    max-height: 100%;
    min-height: calc(100vh - 50px);
    display: grid;
    align-items: stretch;
    grid-template-columns: 5% 1fr 1fr 5%;
    grid-template-rows: 1fr 1fr 1fr 0.5fr;
    grid-template-areas:
      "img img img img"
      ". name name ."
      ". wait info . "
      /*". graph graph ."*/
  }
  .image {
    grid-area: img;
    background-image: url('../assets/hanson-lu-sq5P00L7lXc-unsplash.jpg');
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: flex-end;
  }
  .store-info {
    grid-area: name;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
  }
  .store{
    font-size: 1.5em;
    font-weight: lighter;
    text-transform: capitalize;
  }

  .name {
    font-size: 2em;
    font-weight: bold;
  }

  .waiting {
    grid-area: wait;
    margin: 0.5em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .waiting-number{
    font-size: 4em;
  }
  .waiting-label {
    font-weight: lighter;
    font-size: 2em;
  }
  .chart {
    grid-area: graph;
  }
  .address{
    display: flex;
    justify-content: center;
    margin: 3% 0;
    width: 100%;
  }
  .address > * {
    padding: 0 1%;
    word-break: keep-all;
    text-wrap: avoid;
    height: 1em;
  }
  .shareinfos{
    grid-area: info;
    display: flex;
    justify-content: center;
    align-items: center;
  }

  @media only screen and (min-width: 600px) {
    .infos{
      grid-template-columns: 15% 1fr 1fr 15%;
    }
  }
  @media only screen and (min-width: 1000px) {
    .infos{
      grid-template-columns: 25% 1fr 1fr 25%;
      grid-template-rows: 1fr 1fr 1fr 1fr;
      grid-template-areas:
        "img img img img"
        ". name name ."
        ". wait info . "
        ". graph graph ."
    }
    .waiting-number{
      font-size: 10em;
    }
  }
</style>
