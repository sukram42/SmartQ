<template>
    <div>
      <center>
      <v-app class="shoppanel">
      <h2 class="headerStuff">Hallo! {{ name }} </h2>
        <div :key="shop.id" v-for="shop in shops">
          <shopDetails v-bind:shop="shop"/>
        </div>

            <v-btn class="addBtn" color="cyan" dark fab large position="center" v-bind:to="'newShop/'">
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
  data: () => ({
    name: 'Jürgen Mustermann'
  }),
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
    background: #EEE;
}

.headerStuff {
  background: #DDD;
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
