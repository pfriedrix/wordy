<template>
  <div>
    <Nav />
    <div class="container">
      <div class="section">
        <div class="section__title">Your Collections</div>
      </div>
      <div class="grid" data-column="3" id="grid">
        <template v-if="collections.length > 0">
          <card v-for="collection in collections" :key="collection.id" :title='collection.title' :words='collection.words' :id='collection.id' />
        </template>
        <template v-else><h2 class="no-collections">You don't have collections yet</h2></template>
      </div>
    </div>
    <BottomNav :collections='collections'/>
  </div>
</template>

<script>
import Card from "@/components/CardCollection.vue";
import Nav from "@/components/Nav.vue";
import BottomNav from "@/components/BottomNavHome.vue";

export default {
  components: {
    Card,
    Nav,
    BottomNav
  },
  data: () => ({
    collections: []
  }),
  mounted() {
    this.fetchCollections()
  },
  methods: {
    fetchCollections() {
      this.$store
        .dispatch("getCollections")
        .then(resp => {
          this.collections = resp.data;
        })
        .catch(err => {
          console.log(err);
        });
    }
  }
};
</script>

<style lang="scss" scoped>


.grid {
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
}
.no-collections {
  width: 100%;
  text-align: center;
}
</style>