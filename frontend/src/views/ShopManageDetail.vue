<template>
    <div class="shopHeader">
        <h2>{{shop.name}}</h2>
        <div class="shopDetails">
            <center>
            <table class="editList">
                <tr>
                    <th>Category</th><th><input type="text" v-model="shop.category" readonly="true"/> </th>
                </tr><tr>
                   <th>Address</th><th><input type="text" v-model="shop.address" readonly="true"/> </th>
                </tr><tr>
                  <th>Latitude</th><th><input type="text" v-model="shop.latitude" readonly="true"/> </th>
                </tr><tr>
                  <th>Longditude</th><th><input type="text" v-model="shop.longitude" readonly="true"/> </th>
                </tr><tr>
                  <th>Storespace</th><th><input type="text" v-model="shop.storespace" readonly="true"/> </th>
                </tr><tr>
                  <th>MaxCapacity</th><th><input type="text" v-model="shop.maxcapacity" readonly="true"/> </th>
                </tr><tr>
                  <th>CurrentCapacity</th><th><input type="text" v-model="shop.capacity" readonly="true"/> </th>
                </tr><tr>
                  <th>Waitingtime</th><th><input type="text" v-model="shop.waitingtime" readonly="true"/> </th>
                </tr>
            </table>
            </center>
        <button @click="$emit('edit-shop', shop, this)">Edit</button>
        <button @click="$emit('remove-shop',shop.id)">Remove</button>
        </div>
    </div>
</template>

<script>
export default {
  name: 'ShopDetails',
  props: ['shop']
}
</script>

<style scoped>
.shopHeader{
    background: orangered;
    padding: 10px;
    margin-top: 10px;
    margin-left: 2%;
    margin-right: 2%;

}

.shopDetails{
    background: orange;
    padding: 10px;
}

.editList, th , td {
    border: 1px solid black;
    border-collapse: collapse;
    margin: 5px;
    padding: 5px;
}

</style>
