<template>
  <div id="app">
    <header id="nav">
      <div class="logo">Queueti</div>
      <div class="links">
        <router-link to="/">Home</router-link>
        <router-link to="/shop">Shop</router-link>
      </div>
    </header>
    <div class="content">
      <router-view/>
    </div>

  </div>
</template>

<style lang="scss">
  $header_size: 50px;
  $header_color: #000;
  $header_text_color: #FFF;

  html, body {
    width: 100vw;
    height: 100%;
    max-height: 100%;
    min-height: 100%;
    margin: 0;
  }

  #app {
    font-family: Avenir, Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
  }

  .logo {
    color: white;
    font-size: 2em;
    font-family: fantasy;
    margin: 0 1em;
  }

  .content {
    padding-top: $header_size;
  }

  #nav {
    /*padding: 0 4%;*/
    display: inline-flex;
    position: absolute;
    left: 0;
    top: 0;
    width: 100%;
    min-width: 100%;
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
</style>
