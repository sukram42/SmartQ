<template>
  <div id="app">
    <header id="nav">
      <router-link to="/" class="logo">SmartQ</router-link>
      <div class="links">
        <router-link to="/">Home</router-link>
        <router-link v-if="isLoggedIn" to="/shop">Shop</router-link>
        <router-link  v-if="!isLoggedIn" to="/login">Login</router-link>
        <a v-if="isLoggedIn" @click="logout()">Logout</a>
      </div>
    </header>
    <div class="content">
      <router-view/>
    </div>

  </div>
</template>
<script>
export default {
  name: 'App',
  data: () => ({
    isLoggedIn: window.localStorage.getItem('user') != null
  }),
  methods: {
    logout: function () {
      window.localStorage.removeItem('user')
      this.isLoggedIn = false
      this.$router.push('/login')
    }
  }
}
</script>
<style lang="scss">
  $header_size: 50px;
  $header_color: #000;
  $header_text_color: #FFF;

  html, body {
    width: 100%;
    height: 100%;
    max-width: 100%;
    margin: 0;
    padding: 0;
  }
  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .content {
    padding-top: $header_size;
  }

  #nav {
    display: inline-flex;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    min-width: 100%;
    max-width: 100%;
    height: $header_size;
    background-color: $header_color;
    align-items: center;
    justify-content: space-between;
  }

  .links > * {
    margin: 0 1em;
    color: $header_text_color;
    text-decoration: none;
    font-weight: lighter;
  }
  a{
    &.router-link-exact-active {
      /*Style for active tab*/
      color: #42b983;
    }
  }
  .logo {
    color: white !important;
    text-decoration: none;
    font-size: 2em;
    font-family: fantasy;
    margin: 0 1em;

  }
</style>
