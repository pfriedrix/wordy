<template>
  <div class>
    <Nav />
    <div class="container">
      <div class="section">
        <div class="section__title">Collection - {{ collection.title }}</div>
      </div>
      <div v-if="page == 0">
        <Learn :method='setSnackbar'/>
      </div>
      <div v-if="page == 1" class="grid" data-column="3" id="grid">
          <Card v-for="word in words" :key="word.id" :word='word'/>
      </div>
      <div v-else-if="page == 2">
         <v-expansion-panels>
             <v-expansion-panel>
                 <v-expansion-panel-header><h2>Add word</h2></v-expansion-panel-header>
                 <v-expansion-panel-content>
                   <v-form v-model='valid' @submit.prevent='createWord'>
                     <v-tooltip top>
                       <template v-slot:activator="{ on }">
                         <v-text-field v-model="title"
                            v-on="on"
                            label="Title"
                            :rules="textRules"
                            required
                            solo-inverted
                            @change="translate"
                        ></v-text-field>
                        </template> 
                        <span>to translate press enter</span>
                     </v-tooltip>
                        <v-text-field v-model="translation"
                            label="Translation"
                            :rules="textRules"
                            required
                            solo-inverted></v-text-field>
                        <v-btn width='100%' type='submit' :disabled='!valid'>Create</v-btn>
                   </v-form>
                </v-expansion-panel-content>
             </v-expansion-panel>
             <v-expansion-panel>
                 <v-expansion-panel-header><h2>Delete word</h2></v-expansion-panel-header>
                 <v-expansion-panel-content>
                   <v-form v-model="valid" @submit.prevent='deleteWord'>
                    <v-select solo-inverted label='Choose word' :items='words'
                v-model='word'
                item-text='title'
                return-object></v-select>
                    <v-btn width='100%' type='submit' :disabled='!valid'>Delete</v-btn>.
                   </v-form>
                </v-expansion-panel-content>
             </v-expansion-panel>
             <v-expansion-panel>
                 <v-expansion-panel-header><h2>Edit word</h2></v-expansion-panel-header>
                 <v-expansion-panel-content>
                   <v-form v-model="valid" @submit.prevent='editWord'>
                    <v-select solo-inverted label='Choose word' :items='words' @change="setNewTitle"
                v-model='word'
                item-text='title'
                return-object></v-select>
                <v-tooltip top>
                       <template v-slot:activator="{ on }">
                         <v-text-field v-model="title"
                            v-on="on"
                            label='New title'
                            :rules="textRules"
                            required
                            solo-inverted
                            @change="translate"
                        ></v-text-field>
                        </template> 
                        <span>to translate press enter</span>
                     </v-tooltip>
                        <v-text-field v-model="translation"
                            label="New translation"
                            :rules="textRules"
                            required
                            solo-inverted></v-text-field>
                    <v-btn width='100%' type='submit' :disabled='!valid'>Edit</v-btn>.
                   </v-form>
                </v-expansion-panel-content>
             </v-expansion-panel>
         </v-expansion-panels>
      </div>
    </div>
    <BottomNav :page="page" @changePage="changePage($event)" />
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
  </div>
</template>

<script>
import Nav from "@/components/Nav.vue";
import BottomNav from "@/components/BottomNavCollection.vue";
import Card from "@/components/CardWord.vue";
import Learn from "@/components/Learn.vue"

export default {
  mounted(){
    this.page = this.$route.query.page
    this.getUser()
    this.getCollection()
    this.getWords()
  },
  components: {
    Card,
    Nav,
    BottomNav,
    Learn,
  },
  data: () => ({
    user: '',
    valid: false,
    collection: '',
    words: null,
    word: null,
    bar: false,
    barText: null,
    barColor: '',
    timeout: 0,
    page: null,
    title: '',
    translation: '',
    textRules: [
        v => !!v || 'Title is required',
    ],
  }),
  methods: {
    setSnackbar(text, color, timeout){
      this.barText = text
      this.barColor = color
      this.timeout = timeout
      this.bar = true
    },
    getUser() {
      this.$store.dispatch("getUser")
      .then(resp => this.user = resp.data)
      .catch(err => console.log(err))
    },
    changePage(page) {
      this.page = page;
    },
    getCollection() {
      this.$store.dispatch('getCollection', {
        collection: this.$route.params.id
      })
      .then(resp => {
        this.collection = resp.data
      })
      .catch(err => console.log(err))
    },
    getWords() {
      this.$store.dispatch('getWords', {
        collection: this.$route.params.id
      })
      .then(resp => {
        this.words = resp.data
      })
      .catch(err => console.log(err))
    },
    createWord: function() {
      this.$store.dispatch('createWord', {
        user: this.user.id,
        collection: parseInt(this.$route.params.id),
        title: this.title,
        translation: this.translation,
      })
      .then(() => {
        this.title = '',
        this.translation = '',
        this.valid = false
        window.location.reload()
        
      })
      .catch(err => console.log(err))
    },
    translate: function() {
      this.$store.dispatch('translate', {
        title: this.title,
      })
      .then(resp => {
        this.translation = resp.data.translation
      })
      .catch(err => console.log(err))
    },
    deleteWord: function() {
      this.$store.dispatch('delete', {
        word: this.word.id,
      })
      .then(() => {
        this.word = '',
        this.valid = false
        window.location.reload()
      })
    },
    setNewTitle: function () {
      this.title = this.word.title
    },
    editWord: function () {
      this.$store.dispatch('editWord', {
        user: this.user.id,
        collection: parseInt(this.$route.params.id),
        title: this.title,
        translation: this.translation,
        word: this.word.id,
      })
      .then(() => {
        this.word = '',
        this.title = '',
        this.translation = '', 
        this.valid = false

        window.location.reload()
      })
      .catch(err => console.log(err))
    }
  }
};

</script>

<style lang="scss" scoped>
.container {
  max-width: 1170px;
  width: 100%;
  padding: 0 20px;
  box-sizing: border-box;
  -webkit-transform-origin: top center;
  transform-origin: top center;
  -webkit-transform: scale(0.8);
  transform: scale(0.8);
  .section {
    padding-top: 100px;
    &__title {
      margin: 0 0 70px;
      font-family: "ProximaNovaSoft-Bold" !important;
      font-size: 3.5rem;
      line-height: 2.625rem;
      text-align: center;
    }
  }
}

.grid {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}


.v-expansion-panel {
  max-width: 600px;
}
.v-expansion-panel-content {
    display: flex;
    justify-content: center;
}

</style>