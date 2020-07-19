<template>
  <v-speed-dial
    fixed
    v-model="fab"
    :top="top"
    :bottom="bottom"
    :right="right"
    :left="left"
    :direction="direction"
    :open-on-hover="hover"
    :transition="transition"
  >
    <template v-slot:activator>
      <v-btn v-model="fab" color="#424242" dark fab>
        <v-icon v-if="fab">mdi-close</v-icon>
        <v-icon v-else>mdi-plus</v-icon>
      </v-btn>
    </template>
    <router-link to="/">
      <v-btn fab dark small color="#414141">
        <v-icon>mdi-home</v-icon>
      </v-btn>
    </router-link>

    <router-link to="/profile">
      <v-btn fab dark small color="#414141">
        <v-icon>mdi-account</v-icon>
      </v-btn>
    </router-link>

    <v-btn fab dark small color="#414141">
      <v-icon>mdi-help</v-icon>
    </v-btn>
  </v-speed-dial>
</template>

<script>
export default {
  data: () => ({
    direction: "bottom",
    fab: false,
    fling: false,
    hover: true,
    tabs: null,
    top: true,
    right: true,
    bottom: false,
    left: false,
    transition: "scale-transition"
  }),
  computed: {
    activeFab() {
      switch (this.tabs) {
        case "one":
          return { class: "purple", icon: "account_circle" };
        case "two":
          return { class: "red", icon: "edit" };
        case "three":
          return { class: "green", icon: "keyboard_arrow_up" };
        default:
          return {};
      }
    }
  },
  watch: {
    top(val) {
      this.bottom = !val;
    },
    right(val) {
      this.left = !val;
    },
    bottom(val) {
      this.top = !val;
    },
    left(val) {
      this.right = !val;
    }
  }
};
</script>

<style>
#create .v-speed-dial {
  position: absolute;
}
#create .v-btn--floating {
  position: relative;
}
</style>