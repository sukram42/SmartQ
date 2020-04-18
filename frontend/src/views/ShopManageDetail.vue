<template>
    <div class="shopHeader">
        <h2>{{shop.name}}</h2>
        <div class="shopDetails">
            <center>
            <table class="editList">
                <tr>
                    <th>Category</th><th><v-select :class="{'nonEditText':!editing, 'editText':editing}" v-model="shop.category" :items="categoryItems" :disabled='!editing'/> </th>
                </tr><tr>
                   <th>Address</th><th><v-text-field :class="{'nonEditText':!editing, 'editText':editing}" v-model="shop.address" :disabled='!editing'/> </th>
                </tr><tr>
                  <th>Latitude</th><th><v-text-field :class="{'nonEditText':!editing, 'editText':editing}" v-model="shop.latitude" :disabled='!editing'/> </th>
                </tr><tr>
                  <th>Longditude</th><th><v-text-field :class="{'nonEditText':!editing, 'editText':editing}" v-model="shop.longitude" :disabled='!editing'/> </th>
                </tr><tr>
                  <th>Storespace</th><th><v-text-field :class="{'nonEditText':!editing, 'editText':editing}" v-model="shop.storespace" :disabled='!editing'/> </th>
                </tr><tr>
                  <th>MaxCapacity</th><th><v-text-field :class="{'nonEditText':!editing, 'editText':editing}" v-model="shop.maxcapacity" :disabled='!editing'/> </th>
                </tr><tr>
                  <th>CurrentCapacity</th><th><v-text-field class='nonEditText' v-model="shop.capacity" disabled/> </th>
                </tr><tr>
                  <th>Waitingtime</th><th><v-text-field class='nonEditText' v-model="shop.waitingtime" disabled/> </th>
                </tr>
            </table>
            </center>
            <v-btn class="editButtons" fab dark large color="#2c3e50" v-bind:to="'counter/' + shop.id">
              <v-icon dark>mdi-counter</v-icon>
            </v-btn>
            <v-btn class="editButtons" fab dark large color="#2c3e50" @click="$emit('edit-shop',shop); edit(shop)">
                <v-icon dark>{{editIcon}}</v-icon>
            </v-btn>
            <v-btn class="editButtons" fab dark large color="#2c3e50" @click="$emit('remove-shop',shop)">
                <v-icon dark>mdi-close-outline</v-icon>
            </v-btn>
        </div>
    </div>
</template>

<script>
export default {

  name: 'ShopDetails',
  props: ['shop'],
  data: function () {
    return {
      editing: false,
      categoryItems: ['food', 'groceries', 'restaurant'],
      editIcon: 'mdi-pencil'
    }
  },
  computed: {
  },
  methods: {
    edit (shop) {
      if (this.editing) { // save changes
        this.editIcon = 'mdi-pencil'
        this.editing = false
        // TODO send update to backend
      } else { // go to edit mode
        this.editIcon = 'mdi-content-save'
        this.editing = true
      }
    }
  }
}
</script>

<style>
.v-app{
  min-height: 0px !important;
}
</style>

<style scoped>

.shopHeader{
    background: #6ca39e;
    min-width: 400px;
    padding: 10px;
    margin-top: 10px;
    margin-left: 2%;
    margin-right: 2%;
    border-radius: 30px;
    margin-bottom: 0px;
}

.shopDetails{
    background: #6ca39e;
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
}

.nonEditText{
  background: #AAA;
  border-radius: 20px;
  padding-left: 20px;
  padding-right: 20px;
}

.editText{
  background: #CCC;
  border-radius: 20px;
  padding-left: 20px;
  padding-right: 20px;
}

</style>
