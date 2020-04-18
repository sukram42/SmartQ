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
                  <th>Latitude</th><th><v-text-field class="editText" v-model="latitude" /> </th>
                </tr><tr>
                  <th>Longditude</th><th><v-text-field class="editText" v-model="longitude" /> </th>
                </tr><tr>
                  <th>Storespace</th><th><v-text-field class="editText" v-model="storespace" /> </th>
                </tr><tr>
                  <th>MaxCapacity</th><th><v-text-field class="editText" v-model="maxcapacity" /> </th>
                </tr>
            </table>
            </center>
            <v-btn class="editButtons" fab dark large color="cyan" v-bind:to="'/shop'">
              <v-icon dark>mdi-content-save</v-icon>
            </v-btn>
        </div>
    </v-app>
</div>
</template>

<script>
export default {
  data: function () {
    return {
      categoryItems: ['food', 'groceries', 'restaurant'],
      name: '',
      category: '',
      address: '',
      latitude: '',
      longitude: '',
      storespace: 0,
      maxcapacity: 0
    }
  }
}
</script>

<style scoped>
.shopHeader{
    margin: 0%;
    padding: 30px;
    padding-bottom: 50px;
    background: #2c3e50 !important;
    min-width: 400px;
}

.shopDetails{
    background: #42b983;
    padding: 10px;
    border-radius: 30px;
}

.editList{
    border-collapse: collapse;
    min-width: 300px;
    max-width: 80%;
    width: 70%;
}

.editButtons {
    margin: 10px;
    margin-left: 20px;
    margin-right: 20px;
    color: teal;
}

.editText{
  background: #A4C1BA;
  border-radius: 20px;
  padding-left: 20px;
  padding-right: 20px;
}

</style>
