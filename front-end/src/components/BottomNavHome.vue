<template>
  <div class>
    <v-bottom-navigation dark shift fixed>
      <v-dialog v-model="delCollection" persistent max-width="400px">
        <template v-slot:activator="{ on }">
          <v-btn v-on="on">
            <span>Delete</span>
            <v-icon>mdi-book-remove-multiple</v-icon>
          </v-btn>
        </template>
        <v-form v-model="valid" @submit.prevent="delelteCollection">
          <v-card>
          <v-card-title>
            <span class="headline">Delete</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-select 
                label="Choose collection" 
                solo 
                :rules="rules"
                required
                :items='collections'
                v-model='collection'
                item-text='title'
                return-object
              ></v-select>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn solo @click="delCollection = false">Close</v-btn>
            <v-btn solo color='red' type="submit" :disabled="!valid">Delete</v-btn>
          </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>

      <v-dialog v-model="create" persistent max-width="400px">
        <template v-slot:activator="{ on }">
          <v-btn v-on="on">
            <span>Create</span>
            <v-icon>mdi-book-plus-multiple</v-icon>
          </v-btn>
        </template>
        <v-form v-model="valid" @submit.prevent="createCollection">
          <v-card>
            <v-card-title>
              <span class="headline">Create</span>
            </v-card-title>
            <v-card-text>
              <v-container>
                <v-text-field
                  v-model="collection"
                  label="Title"
                  solo-inverted
                  :rules="rules"
                  required
                ></v-text-field>
              </v-container>
            </v-card-text>
            <v-card-actions>
              <v-spacer></v-spacer>
              <v-btn solo @click="create = false">Close</v-btn>
              <v-btn solo color="success" type="submit" :disabled="!valid">Create</v-btn>
            </v-card-actions>
          </v-card>
        </v-form>
      </v-dialog>

      <v-dialog v-model="edit" persistent max-width="400px">
        <template v-slot:activator="{ on }">
          <v-btn v-on="on">
            <span>Edit</span>
            <v-icon>mdi-book-search</v-icon>
          </v-btn>
        </template>
        <v-form v-model="valid" @submit.prevent="editCollection">
          <v-card>
          <v-card-title>
            <span class="headline">Edit</span>
          </v-card-title>
          <v-card-text>
              <v-container>
                <v-select   
                  label="Choose collection" 
                  solo 
                  :items='collections'
                  v-model='collection'
                  item-text='title'
                  return-object
                  :rules="rules"
                  required
                ></v-select>
                <v-text-field 
                  label="New title" 
                  solo-inverted 
                  v-model='newTitle' 
                  :rules="rules"
                  required
                ></v-text-field>
              </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn solo @click="edit = false">Close</v-btn>
            <v-btn solo color="#414141" type="submit" :disabled="!valid">Edit</v-btn>
          </v-card-actions>
        </v-card>
        </v-form>
        
      </v-dialog>
    </v-bottom-navigation>
  </div>
</template>

<script>
export default {
  props: {
    collections: Array
  },
  data: () => ({
    valid: false,
    create: false,
    newTitle: '',
    delCollection: false,
    edit: false,
    collection: "",
    user: [],
    rules: [v => !!v || "Title is required"]
  }),
  mounted() {
    this.getUser()
  },
  methods: {
    getUser() {
      this.$store.dispatch("getUser")
      .then(resp => this.user = resp.data)
      .catch(err => console.log(err))
    },
    createCollection: function() {
      this.$store
        .dispatch("createCollection", {
          title: this.collection,
          user: this.user.id,
        })
        .then(() => {
          
        })
        .catch(err => {
          console.log(err);
        });
        this.collection = ''
        this.create = false;
        this.valid = false
        window.location.reload()
    },
    delelteCollection: function() {
      this.$store
        .dispatch('delCollection', this.collection.id)
        .then(() => {

        })
        .catch(err => {
          console.log(err)
        })
        this.collection = ''
        this.delCollection = false;
        this.valid = false
        window.location.reload()
    },
    editCollection: function() {
      this.$store
        .dispatch('editCollection', {
          collection: this.collection.id,
          title: this.newTitle,
          user: this.user.id,
        })
        .then(() => {

        })
        .catch(err => {
          console.log(err)
        })
        this.collection = ''
        this.edit = false;
        this.valid = false
        window.location.reload()
    }
  }
};
</script>


