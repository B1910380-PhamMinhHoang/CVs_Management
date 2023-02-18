<script>
import SideBar from "./components/Layout/SideBar.vue";

export default {
  components: {
    SideBar,
  },
  data() {
    return {
      isIntervieweeLogin: false,
    };
  },
};
</script>

<template>
  <div class="d-flex">
    <side-bar class="side-bar" v-if="!isIntervieweeLogin" />
    <router-view
      class="w-100 m-0"
      @intervieweeLogin="isIntervieweeLogin = true"
    />
  </div>
</template>

<style>
.modal-backdrop {
  z-index: -1000 !important;
}

.router-link-exact-active {
  color: gray !important;
  background-color: rgb(206, 198, 198);
}
</style>
