<template>
  <div class="folder p-3 col-sm-6 col-lg-4 col-xl-3">
    <div class="folder-header">
      <div class="row">
        <div class="col-6 p-0 text-success folderId">
          <i
              class="fa-solid fa-copy"
              @click="handleCopyFolderLinkToClipboard"
          ></i>
          UKN
        </div>
        <div class="col-6 p-0">{{ totalCV }} CV</div>
      </div>
    </div>
    <div
      class="folder-name d-flex text-center justify-content-center align-items-center"
      @click="seeCVsInFolder"
    >
      Unknown Folder
    </div>
  </div>
</template>

<script>
export default {
  props: ["totalCV", "folder"],
  data() {
    return {
      folderId: "UKN",
      totalCV: 2,
    };
  },
  methods: {
    handleCopyFolderLinkToClipboard() {
      navigator.clipboard.writeText(
        "http://127.0.0.1:5173/applyCV"
      );
    },
    seeCVsInFolder() {
      this.$router.push({ name: "cvs", params: { folderId: this.folderId } });
    },
  },
};
</script>

<style scoped>
.folder {
  cursor: pointer;
  border-radius: 15px;
}

.fa-copy {
  float: left;
  margin: 5px 0 5px 15px ;
  cursor: pointer;
}

.fa-copy:hover {
  color: black;
}

.folderId {
  overflow: hidden;
  white-space: nowrap;
  color: green;
  font-weight: bold;
}

.folder-header {
  text-align: center;
  font-size: 20px;
  padding: 10px;
  height: 50px;
  background-color: rgb(231, 231, 102);
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.folder-header .x-icon {
  cursor: pointer;
}

.folder-name {
  font-size: 30px;
  padding: 20px;
  height: 150px;
  overflow: hidden;
  background-color: rgb(231, 231, 102);
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}
</style>
