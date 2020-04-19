<template>
    <div>
        <h1>
            Thanks for helping us keep track of waiting persons
        </h1>
        have a great time in our store :)<br/>
        and remember to "check out" when you are done with shoping <br/>
        <v-btn @click="removeUser">I'm done with shoping</v-btn>
    </div>
</template>

<script>
import Axios from 'axios'
import { config } from '../config/config.js'

export default {
  name: 'addUser',
  mounted () {
    console.log(123)
    console.log(this.$route.params.shopID)
    console.log(this.$route.params.userID)
    return Axios.post(`${config.baseApi}/update`, {
      id: parseInt(this.$route.params.shopID),
      peoplechange: 1,
      userid: parseInt(this.$route.params.userID)
    })
  },
  methods: {
    removeUser () {
      return Axios.post(`${config.baseApi}/update`, {
        id: parseInt(this.$route.params.shopID),
        peoplechange: -1,
        userid: parseInt(this.$route.params.userID)
      })
    }
  }
}
</script>
