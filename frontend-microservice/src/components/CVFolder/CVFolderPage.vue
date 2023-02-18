<template>
  <div class="conatiner-fluid">
    <h1 class="pageTitle">Your Folders</h1>
    <div class="folders row p-2">
      <c-v-folder-add
        data-bs-toggle="modal"
        data-bs-target="#addCVFolderModal"
      />
      <c-v-folder-unknown />
      <c-v-folder
        v-for="folder in folders"
        :key="folder._id"
        :totalCV="folder.cvs.length"
        :folder="folder"
        @deleteFolder="deleteFolder(folder._id)"
      />
    </div>
    <c-v-folder-add-modal />
  </div>
</template>

<script>
import CVFolderAdd from "./CVFolderAdd.vue";
import CVFolderUnknown from "./CVFolderUnknown.vue";
import CVFolder from "./CVFolder.vue";
import CVFolderAddModal from "./CVFolderAddModal.vue";

export default {
  components: {
    CVFolderAdd,
    CVFolderUnknown,
    CVFolder,
    CVFolderAddModal,
  },
  data() {
    return {
      folders: [
        {
          _id: "a a a a a a a a a a",
          name: "CTU dsa dsa dsa dsa dsa d",
          cvs: [{}, {}, {}],
        },
        { _id: "b", name: "AU", cvs: [] },
        { _id: "c", name: "BC", cvs: [{}] },
      ],
    };
  },
  methods: {
    deleteFolder(id) {
      this.folders = this.folders.filter((folder) => folder._id != id);
    },
  },
};
</script>

<style scoped>
.pageTitle {
  font-size: 50px;
  margin: 30px;
}

.folders {
  margin: 35px;
  background-color: white;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}
</style>
