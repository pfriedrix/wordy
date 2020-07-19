<template>
  <v-form v-model="valid" @submit.prevent="login">
    <v-container>
      <v-col>
        <h1>Sign In</h1>
        <small>{{ error }}</small>
      </v-col>
      <v-text-field clearable v-model="email" :rules="emailRules" label="E-mail" required solo-inverted></v-text-field>
      <v-text-field
        v-model="password"
        label="Password"
        :rules="passwordRules"
        required
        solo-inverted
        :type="show ? 'text' : 'password'"
        :append-icon="show ? 'mdi-eye' : 'mdi-eye-off'"
         @click:append="show = !show"
      ></v-text-field>
      <v-btn :disabled="!valid" type="submit" solo>Sign In</v-btn>
      <div class="problems">
        <router-link to="/sign-up">
          <h4>Don't have an account?</h4>
        </router-link>

        <h4>or</h4>
        <router-link to="/forget">
          <h4>Forget a password?</h4>
        </router-link>
      </div>
    </v-container>
    <v-snackbar
            top
            v-model="bar"
            :timeout="timeout"
            :color='barColor'
            >
            {{ barText }}
            <v-btn
                color="white"
                text
                @click="bar = false"
            >
                Close
            </v-btn>
            </v-snackbar>
  </v-form>
</template>

<script>
export default {
  data: () => ({

    bar: false,
    barText: null,
    barColor: '',
    timeout: 0,

    loading: false,
    valid: false,
    email: "",
    error: "",
    show: false,
    emailRules: [
      v => !!v || "Email is required",
      v => /.+@.+/.test(v) || "Email must be valid"
    ],
    password: "",
    passwordRules: [
      v => !!v || "Password is required",
      v => (v && v.length >= 8) || "Password must have 8+ characters",
      v => /(?=.*[A-Z])/.test(v) || "Must have one uppercase character",
      v => /(?=.*\d)/.test(v) || "Must have one number"
    ]
  }),
  methods: {
    login: function() {
      (this.loading = true),
        this.$store
          .dispatch("getToken", {
            email: this.email,
            password: this.password
          })
          .then(() => {
            this.$store.dispatch("getUser").then(resp => {
              if (resp.data.is_confirmed == true) {
                this.$router.push("/");
              }
              else {
                this.barText = 'You should confirm your email'
                this.barColor = 'red'
                this.timeout = 0
                this.bar = true
              }
            })
            
          })
          .catch(err => {
            this.error = 'Check your data'
            console.log(err)
          });
      this.loading = false;
    }
  }
};
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