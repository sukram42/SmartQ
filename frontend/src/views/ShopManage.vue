<template>
    <div class='shoppanel'>
      <h2 class="headerStuff">__StoreOwnerX__ </h2>
        <div v-for="shop in shops" :key="shop.id">
          <shopDetails v-bind:shop="shop" v-on:edit-shop="editmode"/>
        </div>
      <v-btn class="addBtn" fab dark large color="cyan" @click="$emit('edit-shop',shop); edit(shop)">
        <v-icon dark>mdi-plus</v-icon>
      </v-btn>
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
    margin: 0%;
    padding: 30px;
    padding-bottom: 50px;
    background: #2c3e50;
}

.headerStuff {
  background: #42b983;
  border-radius: 20px;
  margin: 2%;
  padding: 10px;
}

.addBtn {
  margin: 30px;

}
</style>
