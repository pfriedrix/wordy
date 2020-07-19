<template>
  <v-form v-model="valid" @submit.prevent="register">
    <v-container>
        <v-col>
          <h1>Sign Up</h1>
          <small>{{ text }}</small>
        </v-col>
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            solo-inverted
          ></v-text-field>
          <v-text-field
            v-model="password"
            label="Password"
            :rules="passwordRules"
            required
            solo-inverted
            :type="show1 ? 'text' : 'password'"
            :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show1 = !show1"
          ></v-text-field>
          <v-text-field
            v-model="repassword"
            label="Repeat password"
            :rules="[passwordRules, (this.password === this.repassword) || 'Password must match']"
            required
            solo-inverted
            :type="show2 ? 'text' : 'password'"
            :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
            @click:append="show2 = !show2"
            ref='password'
          ></v-text-field>
          <v-btn
            :disabled="!valid" 
            type="submit"
            native-type='submit'
            :loading='loading'
            solo
          >Sign Up</v-btn>
          <div class="problems">
            <router-link to='/login'>
              <h4>Already have an account?</h4>
            </router-link>
          </div>
          
    </v-container>
  </v-form>
</template>

<script>
  export default {
    data: () => ({
      loading: false,
      valid: false,
      email: '',
      show1: false,
      show2: false,
      text: '',
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
      password: '',
      passwordRules: [
        v => !!v || 'Password is required',
        v => (v && v.length >= 8) || 'Password must have 8+ characters',
        v => /(?=.*[A-Z])/.test(v) || 'Must have one uppercase character',
        v => /(?=.*\d)/.test(v) || 'Must have one number',
      ],
      repassword: '',
    }),
    methods: {
      register: function() {
        let data = {
          email: this.email,
          password: this.password,
          repassword: this.repassword
        }
        this.$store.dispatch('createToken', data)
        .then(() => {
          this.$store.dispatch("getUser")
          this.text = 'Email for confirmation was sent'
        })
        .catch(err => {
          console.log(err)
          this.text = 'Email already exists'
        })
      }
    }
  }
</script>

<style lang="scss" scoped>
form {
  text-align: center;
  width: 400px;
  .v-btn {
    width: 150px;
  }
  .problems {
    margin-top: 40px;
  }
}

</style>