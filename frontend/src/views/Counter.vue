<template>
  <div class="counter-group">
    <div class="error" v-if="error"> {{ error }}</div>
    <div class="count">
      <div class="number">
        {{count}}
      </div>
      <div class="waiting">
        Waiting
      </div>
      <div class="cap" v-if="cap>0">
        {{ cap }} % of {{ maxCap }}
      </div>
      <div class="cap" v-if="cap<=0">
        No
      </div>
      <div class="lblcap">
        People in the Store
      </div>
    </div>
    <div class="btn-down">
      <button v-on:click="()=>onBtnDownClicked()">-</button>
    </div>
    <div class="btn-up">
      <button v-on:click="()=>onBtnUpClicked()">+</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { config } from '../config/config.js'

export default {
  name: 'Counter',
  data: () => ({
    count: 0,
    error: null,
    cap: 0.32,
    maxCap: 200
  }),
  methods: {
    changePeopleCount: function (change) {
      return axios.post(`${config.baseApi}/update`, {
        id: parseInt(this.$route.params.shopID),
        peoplechange: change,
        userid: parseInt(window.localStorage.getItem('user'))
      })
    },
    onBtnUpClicked: function () {
      this.changePeopleCount(1).then(() => this.updateMeasures(true)).catch((e) => {
        this.error = e
      })
    },
    onBtnDownClicked: function () {
      if (this.cap > 0) {
        this.changePeopleCount(-1).then(() => this.updateMeasures(true)).catch((e) => {
          this.error = e
        })
      }
    },
    updateMeasures: async function (countCounting) {
      const answer = await axios.get(`${config.baseApi}/shopinfo?id=${this.$route.params.shopID}&userid=${window.localStorage.getItem('user')}`)

      if (answer.data.length) {
        this.count = countCounting ? answer.data[0].waitingtime : this.count
        this.cap = (answer.data[0].capacity * 100).toFixed(2)
        this.maxCap = answer.data[0].maxcapacity
      }
    }
  },
  async mounted () {
    this.updateMeasures(true)
  }
}
</script>

<style scoped>
  .counter-group{
    display: grid;
    grid-template-columns: 10% 1fr 1fr 10%;
    grid-template-rows: 20% 60% 1fr 10%;
    grid-template-areas:
      " . error error ."
      " . counter2 counter2 ."
      " . counter1 counter3 ."
  ". . . .";
    height: calc(100vh - 50px )
  }
  .btn-up {
    grid-area: counter1;
  }
  button {
    width: 100%;
    height: 100%;
    font-size: 3em;
    background-color: #DDD;
    border-radius: 40px;
  }
  button:active {
    background-color: #EEEEEE;
  }
  .btn-down {
    grid-area: counter3;
  }
  .count {
    grid-area: counter2;
    color: black;
  }
  .number {
    font-size: 10em;
  }
  .error {
    padding: 1em;
    grid-area: error;
    color: red;
    font-size: 1em;
  }
  .waiting {
    font-weight: lighter;
    font-size: 3em;
  }
  .cap{
    font-size: 2em;
    padding-top: 1em;
  }
  .lblcap{
    font-size: 1em;
  }
</style>
