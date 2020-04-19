<template>
  <div>
    <div class="shopList">
      <ShopManage v-bind:shops="shops"/>
    </div>
    {{info}}
  </div>
</template>

<script>
import ShopManage from './ShopManage.vue'
import { config } from '../config/config.js'

import Axios from 'axios'

export default {
  name: 'shop',
  components: {
    ShopManage
  },
  data () {
    return {
      info: null,
      shops: null
    }
  },
  mounted () {
    const user = window.localStorage.getItem('user')
    Axios
      .get(`${config.baseApi}/usershops?id=` + user)
      .then(
        response => {
          const tmp = response.data
          tmp.forEach(element => {
            Axios
              .get(`${config.baseApi}/shopinfo?id=` + element.id)
              .then(
                response => {
                  if (this.shops === null) {
                    this.shops = [response.data[0]]
                  } else {
                    this.shops.push(response.data[0])
                  }
                }
              )
          })
        }
      )
  }
}
</script>

<style>
*{
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}
</style>
