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
    Axios
      .get('http://localhost:5000/shops')
      .then(
        response => {
          console.log(response.data)
          this.shops = response.data
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
