<template>
  <div></div>
</template>

<script>
export default {
  name: 'MapsMarker',
  props: ['lat', 'lng', 'onClick', 'shop', 'color'],
  mounted () {
    this.$parent.getMap(map => {
      this.marker = new window.google.maps.Marker({
        position: { lat: parseFloat(this.lat), lng: parseFloat(this.lng) },
        map: map,
        icon: {
          url: `http://maps.google.com/mapfiles/ms/icons/${this.color ? this.color : 'green'}-dot.png`
        }
      })

      this.marker.addListener('click', () => {
        if (typeof this.onClick === 'function') {
          this.onClick(this.shop)
        }
      })
    })
  },
  beforeDestroy () {
    this.marker.setMap(null)
    window.google.maps.event.clearInstanceListeners(this.marker)
  },
  render () {
    return null
  }
}
</script>

<style scoped>

</style>
