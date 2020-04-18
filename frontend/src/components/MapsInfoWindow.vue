<template>
  <div>
    <slot></slot>
  </div>
</template>

<script>
export default {
  name: 'MapsInfoWindow',
  props: ['lat', 'lng', 'getMap'],
  data: () => ({
    infoW: null
  }),
  methods: {
    closeWindow: () => {
      this.infoW.close()
    },
    openWindow: () => {
      this.$parent.getMap(map => {
        this.infoW.open()
      })
    }
  },
  mounted () {
    this.$parent.getMap(map => {
      (
        this.infoW = new window.google.maps.InfoWindow({
          position: { lat: this.lat, lng: this.lng },
          content: this.$el,
          disableAutoPan: true
        }))
    })
  },
  beforeDestroy () {
    this.infoW.close()
  }
}
</script>

<style scoped>

</style>
