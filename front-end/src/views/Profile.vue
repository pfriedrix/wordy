<template>
  <div>
    <Nav />
    <div class="container">
      <div class="section">
        <div class="section__title">Profile</div>
      </div>
      <v-hover>
        <template v-slot="{ hover }">
          <v-card :elevation="hover ? 24 : 0" class="mx-auto pa-6">
            <v-form v-model="valid" @submit.prevent="editUser">
              <div class="properties">
                <h3>
                  Your firstname:
                  <template v-if="!editFirstname">
                    {{ user.first_name }}
                    <v-btn color="success" width="10" @click="editFirstname = !editFirstname">
                      <v-icon>mdi-pencil</v-icon>
                    </v-btn>
                  </template>
                  <template v-else>
                    <v-text-field
                      label="New"
                      solo-inverted
                      v-model="newFirstname"
                      :rules="rules"
                      required
                    ></v-text-field>
                  </template>
                </h3>
                <h3>
                  Your lastname:
                  <template v-if="!editLastname">
                    {{ user.last_name }}
                    <v-btn color="success" width="10" @click="editLastname = !editLastname">
                      <v-icon>mdi-pencil</v-icon>
                    </v-btn>
                  </template>
                  <template v-else>
                    <v-text-field
                      label="New"
                      solo-inverted
                      v-model="newLastname"
                      :rules="rules"
                      required
                    ></v-text-field>
                  </template>
                </h3>
                <h3>Your e-mail: {{ user.email }}</h3>
                <p>Collections: {{ user.collections.length }}</p>
                <p>Words: {{ user.words.length }}</p>
                <v-btn
                  v-if="editFirstname || editLastname"
                  color="success"
                  width="45%"
                  type="submit"
                  :disabled="!valid"
                >Save</v-btn>
                <v-btn v-if="editFirstname || editLastname" width="45%" @click="shutup">Cancel</v-btn>
              </div>
            </v-form>
          </v-card>
        </template>
      </v-hover>
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
    editLastname: false,
    editFirstname: false,
    newLastname: "",
    newFirstname: "",
    rules: [v => !!v || "Field is required"]
  }),
  mounted() {
    this.getUser();
  },
  methods: {
    getUser() {
      this.$store
        .dispatch("getUser")
        .then(resp => (this.user = resp.data))
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
    }
  }
};
</script>

<style lang="scss" scoped>
.v-card {
  max-width: 500px;
  height: 64vh;
  display: flex;
  align-items: center;
  justify-content: center;
  .propries {
    width: 100%;
  }
}
p {
  margin: 10px;
}
h3 {
  margin-bottom: 10px;
}
.v-btn {
  margin-left: 5px;
}
</style>