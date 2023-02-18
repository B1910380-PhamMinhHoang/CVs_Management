<template>
  <div class="p-3 col-sm-6 col-lg-4 col-xl-3">
    <div class="folder">
      <div class="folder-header">
        <div class="row">
          <div class="col-4 pl-2 folderId">
            <i
              class="fa-solid fa-copy"
              @click="handleCopyFolderLinkToClipboard"
            ></i>
            {{ folder._id }}
          </div>
          <div class="col-5 p-0 font-italic">{{ totalCV }} CV</div>
          <div class="col-3 x-icon" @click="deleteFolder">X</div>
        </div>
      </div>
      <div
        class="folder-name d-flex text-center justify-content-center align-items-center"
        @click="seeCVsInFolder"
      >
        {{ folder.name }}
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["totalCV", "folder"],
  emits: ["deleteFolder"],
  methods: {
    seeCVsInFolder() {
      this.$router.push({ name: "cvs", params: { folderId: this.folder._id } });
    },
    handleCopyFolderLinkToClipboard() {
      navigator.clipboard.writeText(
        "http://127.0.0.1:5173/applyCV?folderId=" + this.folder._id
      );
    },
    deleteFolder() {
      this.$emit("deleteFolder", this.folder._id);
    },
  },
};
</script>

<style scoped>
.folder {
  color: black;
  box-shadow: rgba(17, 17, 26, 0.05) 0px 1px 0px,
    rgba(17, 17, 26, 0.1) 0px 0px 8px;
  border-radius: 15px;
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

.fa-copy {
  float: left;
  margin: 5px;
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

.x-icon {
  cursor: pointer;
  font-size: 20px;
}

.x-icon:hover {
  font-weight: bold;
  color: red;
}

.folder-name {
  cursor: pointer;
  font-size: 25px;
  padding: 20px;
  height: 150px;
  overflow: hidden;
  background-color: rgb(231, 231, 102);
  border-bottom-left-radius: 15px;
  border-bottom-right-radius: 15px;
}
</style>
