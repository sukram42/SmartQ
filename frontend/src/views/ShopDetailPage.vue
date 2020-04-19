<template>
  <div class="infos">
    <div class="image">
      <v-btn @click="()=>$router.go(-1)" class="ma-2" color="orange darken-2" dark>
        <v-icon dark left>mdi-arrow-left</v-icon>Back
      </v-btn>
    </div>
    <div class="store-info" v-if="shop">
      <div class="store" >{{shop.category}}</div>
      <div class="name">{{ shop.name }}</div>
      <div class="address">{{ shop.address }}</div>
    </div>
<!--    <div class="shareinfos" v-on:click="()=>openInMaps()">-->
<!--      <img alt="show on map" src="../assets/iconmonstr-map-8-240.png">-->
<!--      <div> Open in Maps </div>-->
<!--    </div>-->
    <div class="waiting" v-if="shop">
      <div :class="{'indicator': 1, 'indicator-green': shop.waiting < 7 ? 1:0, 'indicator-red': shop.waiting < 7 ? 0:1}"></div>
      <div class="waiting-text">
        <div class="waiting-number"> {{shop.waitingtime}} </div>
        <div class="waiting-label"> Waiting</div>
      </div>
    </div>
    <div class="cap" v-if="shop">
     <div class="cap-text">
        <div class="cap-number"> {{Math.round(shop.capacity*100)}} </div>
        <div class="cap-label"> % Capacity </div>
      </div>
      <div :class="{'indicator': 1, 'indicator-green': shop.capacity < 1 ? 1:0, 'indicator-red': shop.capacity < 1 ? 0:1}"></div>
    </div>
    <div class="chart" v-if="shop">
      <trend
        :data='historyWaiting'
        :gradient="['#b00000', '#ffd05c', '#00b000']"
        :max='shop.maxcapacity'
        :min='shop.maxcapacity'
        strokeWidth="40px"
        auto-draw
        smooth
        >
      </trend>
      <div>
        Current trend of Waiting People
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { config } from '../config/config.js'
import trend from 'vuetrend'

export default {
  name: 'ShopDetailPage',
  data: () => ({
    shop: null,
    // Historic Data
    historyWaiting: []
  }),
  methods: {
    openInMaps: function () {
      window.open(`http://www.google.com/maps/place/${this.shop.latitude},${this.shop.longitude}`)
    },
    loadShopInfo: async function () {
      return axios.get(`${config.baseApi}/shopinfo?id=${this.$route.params.shopID}`)
    }
  },
  async mounted () {
    const shopdata = (await this.loadShopInfo()).data
    this.shop = shopdata[0]
    this.historyWaiting = shopdata.map((datapoint) => datapoint.waitingtime).reverse()
  }
}
</script>

<style scoped>
  svg{
    margin: 0px !important;
    padding: 0px;
    width: 100%;
    height: 100%;
    stroke-width: 1px;
  }
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
    display: grid;
    align-items: stretch;
    grid-template-columns: 5% 1fr 1fr 5%;
    grid-template-rows: 1fr 1fr 1fr 0.5fr;
    grid-template-areas:
      "img img img img"
      ". name name ."
      ". wait info . "
      ". graph graph ."
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
    padding: 4% 0 0 0;
    flex-direction: column;
    justify-content: flex-start;
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
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
  }
  .waiting-text{
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
    font-size: 1.4em;
  }
  .chart {
    grid-area: graph;
    margin-top: 10%
  }
  .address{
    padding-top: 2%;
  }
  .address > * {
    padding: 0 1%;
    word-break: keep-all;
    text-wrap: avoid;
  }
  .indicator {
    width: 1em;
    height: 7em;
    margin-right: 1em;
  }
  .indicator-green {
    background-color: #42b983;
  }
  .indicator-red {
    background-color: #B9584A;
  }
  .cap {
    grid-area: info;
    margin: 0.5em;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
  }
  .cap-text{
    margin: 0.5em;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
  }
  .cap-number{
    font-size: 4em;
  }
  .cap-label {
    font-weight: lighter;
    font-size: 1.4em;
  }

  .shareinfos{
    grid-area: info;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
  }
  .shareinfos > div {
    padding-top: 1em;
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
