<template>
    <div class="column">
        <div class="content">
            <div class="content__name">{{ title }}</div>
            <div class="content__title">Words: {{ words.length }}</div>
        </div>
        <div class="navigation">
            <router-link class="navigation__item" :to="{ name: 'collection', params: { id: id }, query: { page: 1}}"><v-icon large='true' color="#414141" >{{ collection }}</v-icon></router-link>
            <router-link class="navigation__item" :to="{ name: 'collection', params: { id: id }, query: { page: 0}}"><v-icon large='true' color="#414141">{{ practise }}</v-icon></router-link>
        </div>
    </div>
</template>
<script>
import { mdiBookAlphabet, mdiBrain } from '@mdi/js';

export default {
    props: {
      title: String,
      words: Array,
      id: Number,
    },
    data: () => ({

       collection: mdiBookAlphabet,
       practise: mdiBrain,
    }),
    
}
</script>

<style lang="scss" scoped>
.column {

    height: 400px;
    position: relative;
    z-index: 0;
    border: none;
    box-sizing: border-box;
    transition: box-shadow 0.2s ease, z-index 0s 0.2s ease,
      -webkit-transform 0.2s ease;
    transition: box-shadow 0.2s ease, transform 0.2s ease, z-index 0s 0.2s ease;
    transition: box-shadow 0.2s ease, transform 0.2s ease, z-index 0s 0.2s ease,
      -webkit-transform 0.2s ease;
    &:before {
      content: "";
      display: block;
      padding-top: 100%;
    }
    &:hover {
      z-index: 1;
      box-shadow: 0 8px 50px rgba(0, 0, 0, 0.2);
      -webkit-transform: scale(1.05);
      transform: scale(1.05);
      transition: box-shadow 0.2s ease, z-index 0s 0s ease,
        -webkit-transform 0.2s ease;
      transition: box-shadow 0.2s ease, transform 0.2s ease, z-index 0s 0s ease;
      transition: box-shadow 0.2s ease, transform 0.2s ease, z-index 0s 0s ease,
        -webkit-transform 0.2s ease;
    }
    &:hover .navigation {
      opacity: 1;
    }
    .content {
      position: absolute;
      top: 50%;
      left: 0;
      width: 100%;
      -webkit-transform: translate(0, -50%);
      transform: translate(0, -50%);
      text-align: center;
      &__name {
        font-family: "ProximaNovaSoft-Medium";
        font-size: 2rem;
        line-height: 2.625rem;
      }
      &__title {
        font-family: "ProximaNovaSoft-Medium";
        font-size: 1.275rem;
        line-height: 2.375rem;
      }
    }
    .navigation {
      opacity: 0;
      position: absolute;
      bottom: 20px;
      width: 100%;
      &__item {
        position: absolute;
        display: inline-block;
        font-family: "ProximaNovaSoft-Regular";
        text-decoration: none;
        font-size: 25px;
        color: #000;
        bottom: 0;
        margin-left: 30px;
        &:last-child {
          right: 30px;
        }
        &:hover {
          transform: scale(1.4);
          transition: 0.3s transform;
          color: rgb(22, 22, 22);
        }
      }
    }
  }


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

</style>