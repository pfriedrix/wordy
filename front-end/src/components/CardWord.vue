<template>
  <div class="column">
    <v-card class="mx-auto" width="320">
      <v-card-title>{{ word.title | toLower }}</v-card-title>
      <v-card-actions>
        <v-btn color="purple" text @click="translation = !translation">Translate</v-btn>
        <v-btn color="purple" text @click="progress = !progress">Progress</v-btn>
        <v-spacer></v-spacer>
      </v-card-actions>

      <v-expand-transition>
        <div v-show="translation">
          <v-divider></v-divider>
          <v-card-text class="text-center">{{ word.translation | toLower }}</v-card-text>
        </div>
      </v-expand-transition>
      <v-expand-transition>
        <div v-show="progress">
          <v-divider></v-divider>
          <v-card-text>
            <v-progress-linear active :value="word.progress"></v-progress-linear>
          </v-card-text>
        </div>
      </v-expand-transition>
    </v-card>
  </div>
</template>
<script>
export default {
  props: {
    word: Object,
  },
  data: () => ({
    translation: false,
    progress: false,
  }),
  filters: {
    toLower: function(value) {
      return value.toLowerCase()
    }
  }
};
</script>

<style lang="scss" scoped>

.grid[data-column="1"] .column {
  width: 100%;
  max-width: 100%;
  min-width: 100%;
  flex-basis: 100%;
}
.grid[data-column="2"] .column {
  width: 50%;
  max-width: 50%;
  min-width: 50%;
  flex-basis: 50%;
}
.grid[data-column="3"] .column {
  width: 33.3333333333%;
  max-width: 33.3333333333%;
  min-width: 33.3333333333%;
  flex-basis: 33.3333333333%;
}
.grid[data-column="4"] .column {
  width: 25%;
  max-width: 25%;
  min-width: 25%;
  flex-basis: 25%;
}
.grid[data-column="5"] .column {
  width: 20%;
  max-width: 20%;
  min-width: 20%;
  flex-basis: 20%;
}
.grid[data-column="6"] .column {
  width: 16.6666666667%;
  max-width: 16.6666666667%;
  min-width: 16.6666666667%;
  flex-basis: 16.6666666667%;
}
.grid[data-column="7"] .column {
  width: 14.2857142857%;
  max-width: 14.2857142857%;
  min-width: 14.2857142857%;
  flex-basis: 14.2857142857%;
}
.grid[data-column="8"] .column {
  width: 12.5%;
  max-width: 12.5%;
  min-width: 12.5%;
  flex-basis: 12.5%;
}
.grid[data-column="9"] .column {
  width: 11.1111111111%;
  max-width: 11.1111111111%;
  min-width: 11.1111111111%;
  flex-basis: 11.1111111111%;
}

@media (max-width: 800px) {
  .column {
    width: 50% !important;
    max-width: 50% !important;
    min-width: 50% !important;
    flex-basis: 50% !important;
  }
}
@media (max-width: 600px) {
  .column {
    width: 100% !important;
    max-width: 100% !important;
    min-width: 100% !important;
    flex-basis: 100% !important;
  }
}

.column {
    margin-bottom: 20px;
    margin-right: 20px;
}
</style>