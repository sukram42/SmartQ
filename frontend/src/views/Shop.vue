<template>
  <div>
    <div class="shopList">
      <ShopManage v-bind:shops="shops" v-on:add-shop="addShop"/>
    </div>
  </div>
</template>

<script>
import ShopManage from './ShopManage.vue'

export default {
  name: 'shop',
  components: {
    ShopManage
  },
  data () {
    return {
      shops: [
        {
          id: 1,
          name: 'Emmas Ramsch',
          category: 'groceries',
          address: 'Musterstraße 7, 80807 München',
          latitude: '48.2',
          longitude: '11.5',
          storespace: 800,
          maxcapacity: 50,
          capacity: 13,
          waitingtime: 5
        },
        {
          id: 2,
          name: 'Eisdiele um die Ecke',
          category: 'ice',
          address: 'Musterstraße 8, 80807 München',
          latitude: '48.21',
          longitude: '11.5',
          storespace: 60,
          maxcapacity: 3,
          capacity: 1,
          waitingtime: 14
        }
      ]
    }
  },
  methods: {
    addShop () {
      console.log('add A Shop')
      this.shops.push(
        {
          id: 0,
          name: '',
          category: '',
          address: '',
          latitude: '',
          longitude: '',
          storespace: 0,
          maxcapacity: 0,
          capacity: 0,
          waitingtime: 0
        })
    }
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
