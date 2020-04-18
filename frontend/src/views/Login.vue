<template>
  <div class="login">
  <div class="login-fields" v-if="isLogging">
    <h1>Login</h1><br />
    <p>
      You have a little store and want to be a part of <b>SmartQ</b>? <a @click="isLogging=!isLogging">Register here!</a>
    </p>
    <v-text-field label="name" v-model="name"></v-text-field>
    <v-text-field
      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
      :type="show1 ? 'text' : 'password'"
      @click:append="show1 = !show1"
      counter
      label="Password"
      name="input-10-1"
      v-model="password"
    ></v-text-field>
    <v-btn :disabled="isBtnDisabled" class="submit-button">Go!</v-btn>
  </div>
  <div class="register-fields" v-if="!isLogging">
    <h1>Register</h1>
    <br>
    <p>
      Already have an <b>SmartQ</b> account.<br> <a @click="isLogging=!isLogging">Log in right here.</a><br>
    </p>

    <v-text-field label="name" v-model="name"></v-text-field>
    <v-text-field
      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
      :type="show1 ? 'text' : 'password'"
      @click:append="show1 = !show1"
      counter
      label="Password"
      name="input-10-1"
      v-model="password"
    ></v-text-field>
    <v-text-field
      :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
      :type="show1 ? 'text' : 'password'"
      @click:append="show1 = !show1"
      counter
      label="Repeat Password"
      name="input-10-1"
      v-model="password2"
    ></v-text-field>
    <v-btn :disabled="isBtnDisabled" class="submit-button">Go!</v-btn>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Login',
  data: () => ({
    isLogging: true,
    availableBtn: false,
    password: '',
    password2: '',
    name: '',
    firstName: '',
    show1: false,
    rules: {
      required: value => !!value || 'Required.',
      emailMatch: () => ('The email and password you entered don\'t match')
    }
  }),
  computed: {
    isBtnDisabled: function () {
      return !(this.password.length > 0 && (this.isLogging || this.password === this.password2) && this.name.length > 0)
    }
  }
}
</script>

<style scoped>
  a {
    color: #00D;
  }
  p{
    padding-bottom: 1em;
  }
  .login{
    display: grid;
    grid-template-columns: 10% auto 10%;
    grid-template-rows: 10% auto 50%;
    grid-template-areas:
  ". . ."
  ". fields ."
  ". . .";
  }
  .login-fields, .register-fields {
    min-width: 80%;
    grid-area: fields;
    background-color: #EEE;
    display: flex;
    flex-direction: column;
    padding: 1em
  }
  .submit-button {
    margin-top: 1em;
  }
</style>
