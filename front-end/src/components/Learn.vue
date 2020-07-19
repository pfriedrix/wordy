<template>
  <div class="learn-page">
    <v-btn color="success" v-if="!start" @click="start = !start">Start!</v-btn>
    <v-stepper v-model="step" v-if="start">
      <template v-if="words">
         <h3 v-if="!words.length > 0" class="text-center">You don't have engough words in collection or learnt everything</h3>
        <v-stepper-header>
          <template v-for="n in steps">
            <v-stepper-step :key="`${n}-step`" :complete="step > n" :step="n" :editable="editable"></v-stepper-step>

            <v-divider v-if="n !== steps" :key="n"></v-divider>
          </template>
        </v-stepper-header>

        <v-stepper-items>
          <v-stepper-content
            v-for="(word, index) in words"
            :key="`${index+1}-content`"
            :step="index+1"
          >
            <v-card elevation="7">
              <v-card-title>
                {{ word.translation }}
              </v-card-title>
              <v-card-subtitle>
                Choose correct translation
              </v-card-subtitle>
              
              <v-card-text>
                <template v-if="!visible">
                  <v-btn v-for="option in options" :key="option" @click="checkAnswer(option.toLowerCase())">{{ option}}</v-btn>
                </template>  
                <template v-else>
                  <v-btn v-for="option in options" :color="setColor(option)" :key="option">{{ option}}</v-btn>
                </template>
              </v-card-text>
                
            </v-card>

            <v-btn v-if="visible" color="primary" @click="nextStep(index+1)">{{ text }}</v-btn>

            <v-btn @click="start = !start">Cancel</v-btn>
          </v-stepper-content>
        </v-stepper-items>
      </template>
    </v-stepper>
  </div>
</template>

<script>
export default {
  props: {
    method: Function,
  },
  data() {
    return {
      text: 'continue',
      visible: false,
      step: 1,
      start: false,
      words: [],
      steps: 0,
      options: [],
      origin: '',
      answer: '',
    };
  },
  mounted() {
    this.getWords();
  },
  methods: {
    getWords() {
      this.$store
        .dispatch("getRandomWords", {
          collection: parseInt(this.$route.params.id)
        })
        .then(resp => {
          this.words = resp.data.words;
          if (resp.data.words.length > 0) {
            this.getOptions(resp.data.words[0].id)
          }
          this.steps = resp.data.words.length
        })
        .catch(err => {
          console.log(err);
        });
    },
    nextStep(n) {      
      this.options = ''
      this.origin = ''
      if (n + 1 === this.steps) {
        this.text = 'finish'
      }
      if (n === this.steps) {
         window.location.reload()
      } else {
        this.step = n + 1;
      }
      this.getOptions(this.words[n].id)
      this.visible = false
      
    },
    getOptions(id) {
      this.$store.dispatch('getOptions', {
        word: id
      })
      .then(resp => {
        this.options = resp.data.options
        this.origin = resp.data.origin
      })
    },
    checkAnswer(value) {
      this.answer = value.toLowerCase()
      if (value.toLowerCase() === this.origin.title.toLowerCase()) {
        this.$store.dispatch('learnWord', {
          word: this.origin.id
        })
        .catch(err => console.log(err))
        this.method('You have earnt 10xp', 'success', 4000)
      }else {
        this.method('You are wrong', 'red', 4000)
      }
      this.visible = true
    },
    setColor(value) {
      if (value.toLowerCase() === this.origin.title.toLowerCase()){
        return 'success'
      } else if (value === this.answer){
        return 'red'
      } else {
        return null
      }
    }
  },
  watch: {
    steps(val) {
      if (this.e1 > val) {
        this.step = val;
      }
    }
  }
};
</script>

<style lang="scss" scoped>
.learn-page {
  display: flex;
  height: 55vh;
  align-items: center;
  justify-content: center;
}
.v-stepper {
  width: 100%;
}
.v-card {
  padding: 20px;
  margin: 30px;
  height: 100%;
}
.v-btn {
  margin: 5px;
}
</style>