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
    error: null
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
      this.changePeopleCount(1).then(() => {
        // TODO Add the update
      }).catch((e) => {
        this.error = e
      })
      this.count += 1
    },
    onBtnDownClicked: function () {
      this.changePeopleCount(1).then(() => {
        // TODO Add the update
      }).catch((e) => {
        this.error = e
      })
      this.count -= this.count > 0 ? 1 : 0
    }
  },
  async mounted () {
    // this.count = await axios.get('')
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
</style>
