<template>
  <div class="folder p-3 col-sm-6 col-lg-4 col-xl-3">
    <div class="folder-header">Add a folder</div>
    <div class="folder-name d-flex justify-content-center align-items-center">
      +
    </div>
  </div>
</template>

<script>
export default {
  props: ["totalCV", "folderName"],
};
</script>

<style scoped>
.folder {
  cursor: pointer;
  border-radius: 15px;
}

.folder:hover {
  opacity: 0.6;
}

.folder-header {
  text-align: center;
  font-size: 20px;
  padding: 10px;
  height: 50px;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
  background-color: gainsboro;
}

.folder-header .x-icon {
  float: right;
}

.folder-name {
  text-align: center;
  align-items: center;
  font-size: 50px;
  padding: 20px;
  height: 150px;
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
  background-color: gainsboro;
}
</style>
