<template>
    <div class='shoppanel'>
        You are logged in as __StoreOwnerX__
       <div v-for="shop in shops" :key="shop.id">
           <shopDetails v-bind:shop="shop" v-on:edit-shop="editmode"/>
       </div>
    </div>
</template>

<script>
import shopDetails from './ShopManageDetail'
export default {
  name: 'ShopManage',
  components: {
    shopDetails
  },
  methods: {
    editmode (id) {
      console.log('Open edit page') //  TODO
    }
  },
  props: ['shops']
}
</script>

<style scoped>
.shoppanel {
    margin-left: 2%;
    margin-right: 2%;
    margin-top: 2%;
    padding: 30px;
    padding-bottom: 50px;
    background: orchid;
}
</style>
