<template>
    <div>
      <center>
      <v-app class="shoppanel">
      <h2 class="headerStuff">__StoreOwnerX__ </h2>
        <div v-for="shop in shops" :key="shop.id">
          <shopDetails v-bind:shop="shop"/>
        </div>

            <v-btn class="addBtn" position="center" fab dark large color="cyan" v-bind:to="'newShop/'">
              <v-icon dark>mdi-plus</v-icon>
            </v-btn>
      </v-app>
      </center>
    </div>
</template>

<script>
import shopDetails from './ShopManageDetail'
export default {
  name: 'ShopManage',
  components: {
    shopDetails
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
  margin-left: auto;
  margin-right: auto;
}
</style>
