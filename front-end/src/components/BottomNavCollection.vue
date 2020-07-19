<template>
  <div class>
    <v-bottom-navigation :v-model="bottomNav" dark shift fixed>
      <v-btn @click='changePage("0")'>
        <span>Learn</span>
        <v-icon>mdi-brain</v-icon>
      </v-btn>
      <v-btn @click='changePage("1")'>
        <span>Words</span>
        <v-icon>mdi-view-list</v-icon>
      </v-btn>
      <v-btn @click='changePage("2")'>
        <span>Manage</span>
        <v-icon>mdi-cog</v-icon>
      </v-btn>
    </v-bottom-navigation>
  </div>
</template>

<script>
export default {
  props: {
    page: String
  },
  data: () => ({
    bottomNav: '',
  }),
  methods: {
      changePage(page) {
        this.$emit('changePage', page)
      }
  }
};
</script>


