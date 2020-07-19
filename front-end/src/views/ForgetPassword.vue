<template>
  <v-form v-model="valid">
    <v-container>
        <v-col>
          <h1>Reset Password</h1>
        </v-col>
          <v-text-field
            v-model="email"
            :rules="emailRules"
            label="E-mail"
            required
            solo-inverted
          ></v-text-field>
          <v-btn
            native-type='submit'
            :loading='loading'
            solo
          >Send Mail</v-btn>
          <div class="problems">
              <router-link to='/sign-up'>
                  <h4>Want to create new?</h4>
              </router-link>
            
            <h4>or</h4>
            <router-link to='/login'>
                <h4>Rememver a password?</h4>
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
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
    }),
    
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