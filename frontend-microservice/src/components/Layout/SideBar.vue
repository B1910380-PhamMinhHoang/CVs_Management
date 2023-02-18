<template>
  <nav :class="{ showNavCSS: isShowNav, hideNavCSS: !isShowNav }">
    <i
      class="nav-arrow fa-solid fa-arrow-left"
      @click="toggleShowNav"
      v-if="isShowNav"
    ></i>
    <i
      class="nav-arrow fa-solid fa-arrow-right"
      @click="toggleShowNav"
      v-else
    ></i>

    <div v-if="isShowNav">
      <h1 class="my-3">My app</h1>
      <ul>
        <li>
          <router-link :to="{ name: 'folders' }">
            <i class="fa-solid fa-folder"></i> Folders
          </router-link>
        </li>
        <li>
          <router-link :to="{ name: 'applyCVForm' }">
            <i class="fa-solid fa-folder"></i> Form apply CV
          </router-link>
        </li>
      </ul>
    </div>
  </nav>
</template>

<script>
export default {
  data() {
    return {
      isShowNav: true,
    };
  },
  methods: {
    toggleShowNav() {
      this.isShowNav = !this.isShowNav;
    },
  },
};
</script>

<style scoped>
nav {
  min-height: 100vh;
  transition: width 2s;
  position: relative;
  background-color: rgb(158, 151, 151);
}

.fa-arrow-left {
  position: absolute;
  right: 0;
  z-index: 1;
}

.fa-arrow-right,
.fa-arrow-left {
  padding: 10px;
  border-radius: 50%;
  color: white;
}

.fa-arrow-right:hover,
.fa-arrow-left:hover {
  color: black;
  cursor: pointer;
}

.showNavCSS {
  width: 400px;
}

.hideNavCSS {
  width: 60px;
}

.nav-arrow {
  font-size: 20px;
  margin: 10px;
}

h1 {
  padding: 15px 25px;
  color: greenyellow;
  font-weight: bold;
}

ul {
  list-style-type: none;
  padding: 0;
}

ul li a {
  display: block;
  padding: 12px 25px;
  cursor: pointer;
  font-size: 22px;
  font-weight: bold;
  text-decoration: none;
  color: whitesmoke;
}

ul li a:hover {
  background-color: rgb(141, 137, 137);
}

ul li i {
  margin: 0 10px;
}
</style>
