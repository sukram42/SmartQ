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
    const user = window.localStorage.getItem('user')
    Axios
      .get('http://localhost:5000/usershops?id=' + user)
      .then(
        response => {
          console.log(response.data)
          console.log(window.localStorage.getItem('user'))
          const tmp = response.data
          tmp.forEach(element => {
            Axios
              .get('http://localhost:5000/shopinfo?id=' + element.id)
              .then(
                response => {
                  console.log(response.data[0])
                  if (this.shops === null) {
                    this.shops = [response.data[0]]
                  } else {
                    this.shops.push(response.data[0])
                  }
                }
              )
            console.log('asdasd' + element.id)
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
