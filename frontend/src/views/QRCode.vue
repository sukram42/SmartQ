<template>
  <div class="qrCode">
    <h3>Scan this if you want to join the Queue of this Store:</h3> <br/>
    <qrcodevue :value="qradd" size="400"></qrcodevue>
  </div>
</template>

<script>
import Qrcodevue from 'qrcode.vue'

export default {
  name: 'QRCode',
  data: () => ({
    qradd: 'http://dies-das-ananas.net/addUser?id=3&userid=3'
  }),
  components: {
    Qrcodevue
  },
  mounted () {
    this.qradd = 'http://dies-das-ananas.net/addUser?id=' + this.$route.params.shopID + '&userid=' + window.localStorage.getItem('user')
  }
}
</script>

<style scoped>

</style>
