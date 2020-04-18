<template>
  <div class="counter-group">

    <div class="count">
      <div class="number">
        999
      </div>
      <div class="waiting">
        Waiting
      </div>
    </div>
    <div class="btn-down">
      <button>-</button>
    </div>
    <div class="btn-up">
      <button>+</button>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Counter'
}
</script>

<style scoped>
  .counter-group{
    display: grid;
    grid-template-columns: 10% 1fr 1fr 10%;
    grid-template-rows: 20% 60% 1fr 10%;
    grid-template-areas:
      " . . . ."
      " . counter2 counter2 ."
      " . counter1 counter3 ."
  ". . . .";
    height: calc(100vh - 50px )
  }
  .btn-up {
    grid-area: counter1;
  }
  button {
    width: 100%;
    height: 100%;
    font-size: 3em;
    background-color: #DDD;
    border-radius: 40px;
  }
  button:active {
    background-color: #EEEEEE;
  }
  .btn-down {
    grid-area: counter3;
  }
  .count {
    grid-area: counter2;
    color: black;
  }
  .number {
    font-size: 10em;
  }
  .waiting {
    font-weight: lighter;
    font-size: 3em;
  }
</style>
