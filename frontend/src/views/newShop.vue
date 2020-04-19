<template>
<div class="shopHeader">
    <v-app class="shopHeader">
        <div class="shopDetails">
            <center>
            <table class="editList">
                <tr>
                    <th>Name</th><th><v-text-field class="editText" v-model="name" /> </th>
                </tr><tr>
                    <th>Category</th><th><v-select class="editText" v-model="category" :items="categoryItems"/> </th>
                </tr><tr>
                   <th>Address</th><th><v-text-field class="editText" v-model="address" /> </th>
                </tr><tr>
                  <th>Storespace</th><th><v-text-field class="editText" v-model="storespace" /> </th>
                </tr><tr>
                  <th>MaxCapacity</th><th><v-text-field class="editText" v-model="maxcapacity" /> </th>
                </tr>
            </table>
            </center>
            <v-btn class="editButtons" fab dark large color="cyan" @click="uploadShop">
              <v-icon dark>mdi-content-save</v-icon>
            </v-btn>
        </div>
    </v-app>
</div>
</template>

<script>
import Axios from 'axios'
import { config } from '../config/config.js'
export default {
  data: function () {
    return {
      categoryItems: ['food', 'groceries', 'restaurant'],
      name: '',
      category: '',
      address: '',
      storespace: 0,
      maxcapacity: 0
    }
  },
  methods: {
    uploadShop () {
      Axios
        .post(`${config.baseApi}/shopinfo`, {
          name: this.name,
          category: this.category,
          address: this.address,
          storespace: this.storespace,
          maxcapacity: this.maxcapacity,
          userid: window.localStorage.getItem('user')
        }
        )
        .then(this.$router.push('/shop'))
    }
  }
}
</script>

<style scoped>
.shopHeader{
    margin: 0%;
    padding: 30px;
    padding-bottom: 50px;
    background: #DDD !important;
    min-width: 350px;
}
.shopDetails{
    background: #6ca39e;
    padding: 10px;
    border-radius: 30px;
}

.editList{
    border-collapse: collapse;
    min-width: 260px;
    max-width: 80%;
    width: 70%;
}

.editButtons {
    margin: 10px;
    margin-left: 20px;
    margin-right: 20px;
}

.editText{
  background: #CCC;
  border-radius: 20px;
  padding-left: 20px;
  padding-right: 20px;
}

</style>
