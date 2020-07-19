<template>
  <v-app>
    
    <component :is='layout'> 
      <router-view/>
    </component>
  </v-app>
</template>

<script>
import EntryLayout from '@/layouts/EntryLayout.vue'
import EmptyLayout from '@/layouts/EmptyLayout.vue'

export default {
  computed: {
    layout(){
      return this.$route.meta.layout + '-layout'
    },
  },
  components: {
    EntryLayout, EmptyLayout, 
  }

};
</script>

<style lang="scss">
@import '@/assets/styles/style.scss';
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

</style>