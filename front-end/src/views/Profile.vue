<template>
  <div>
    <Nav />
    <div class="container">
      <div class="section">
        <div class="section__title">My profile</div>
        <v-row justify='center'>
          <v-card
          elevation="10"
          height="500"
          color="black"
          shaped
          style="color:white;"
          width='400'
        >
          <div class="headline text-center">
            <h3>{{user.first_name}} {{user.last_name}}</h3>
            <h2>{{user.age}}</h2>
            <v-row justify="center">
              <div right style="margin-right: 40px;">
                <v-icon x-large color="white">mdi-brain</v-icon>
                x {{learntWords}}
              </div>
              <div left>
                <v-icon x-large color="white">mdi-book</v-icon>
                x {{user.collections.length}}
              </div>
            </v-row>
            <v-row justify="center">
              <v-icon x-large color='white'>mdi-puzzle-star</v-icon> x {{ xps }}
            </v-row>
          </div>
        </v-card>
        </v-row>
      </div>
    </div>
  </div>
</template>

<script>
import Nav from "@/components/Nav.vue";
export default {
  components: {
    Nav
  },
  data: () => ({
    valid: false,
    user: null,
    learntWords: 0,
    editLastname: false,
    editFirstname: false,
    newLastname: "",
    newFirstname: "",
    xps: 0,
    rules: [v => !!v || "Field is required"]
  }),
  mounted() {
    this.getUser();
  },
  methods: {
    getUser() {
      this.$store
        .dispatch("getUser")
        .then(resp => {
          this.user = resp.data;
          this.getLearntWords(this.user.words);
          this.getXPS();
        })
        .catch(err => console.log(err));
    },
    shutup: function() {
      this.editFirstname = false;
      this.editLastname = false;
      this.newLastname = "";
      this.newFirstname = "";
    },
    editUser: function() {
      if (this.newLastname !== "" && this.newFirstname !== "") {
        this.$store
          .dispatch("editUser", {
            first_name: this.newFirstname,
            last_name: this.newLastname
          })
          .then(() => window.location.reload())
          .catch(err => console.log(err));
      } else if (this.newLastname === "" && this.newFirstname !== "") {
        this.$store
          .dispatch("editUser", {
            first_name: this.newFirstname
          })
          .then(() => window.location.reload())
          .catch(err => console.log(err));
      } else {
        this.$store
          .dispatch("editUser", {
            last_name: this.newLastname
          })
          .then(() => window.location.reload())
          .catch(err => console.log(err));
      }
    },
    getLearntWords: function() {
      this.$store
        .dispatch("getLearntWords")
        .then(resp => {
          this.learntWords = resp.data.length;
        })
        .catch(err => console.log(err));
    },
    getXPS: function() {
      this.$store.dispatch('getXPS')
      .then(resp => this.xps = resp.data.xps)
    }
  }
};
</script>

<style lang="scss" scoped>
.headline {
  padding-top: 100px;
}
.row {
  margin-top: 30px;
}
.v-card {
  margin-top: 30px;
}

</style>