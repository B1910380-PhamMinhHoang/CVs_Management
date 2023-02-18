<template>
  <div>
    <div class="formApplyCV mx-auto my-5 fw-bold">
      <div v-if="!isIntervieweeLogin && isModifyTitle" class="d-flex justify-content-between">
        <input type="text" class="form-control w-75" v-model="formTitle" />
        <button 
          class="btn btn-warning fw-bold"
          @click="handleSaveTitle"
        >
          <i class="fa-solid fa-floppy-disk"></i> Save
        </button>
      </div>
      <h1 v-else id="title" class="mb-2">
        {{ formTitle }}
        <button 
          class="btn btn-primary fw-bold"
          @click="handleModifyTitle"
          v-if="!isIntervieweeLogin"
        >
          <i class="fa-solid fa-pencil"></i> Modify
        </button>
      </h1>
      <hr />
      <div class="mb-4">
        <label for="nameInput" class="form-label">Your name:</label>
        <input type="text" class="form-control" id="nameInput" />
      </div>
      <div class="mb-4">
        <label for="phoneNumberInput" class="form-label"
          >Your phone number:</label
        >
        <input type="number" class="form-control" id="phoneNumberInput" />
      </div>
      <div class="mb-5">
        <label for="emailInput" class="form-label">Your email:</label>
        <input type="text" class="form-control" id="emailInput" />
      </div>
      <div class="mb-5">
        <label for="cvFileUploadInput" id="cvFileUploadLabel"
          >Upload your CV
          <i class="fa-solid fa-upload float-end"></i>
        </label>
        &nbsp;&nbsp;&nbsp;&nbsp;
        <input
          type="file"
          id="cvFileUploadInput"
          class="d-none"
          @change="handleCVFileUpload"
        />
        <span id="cvFileName">{{ cvFileName }}</span>
      </div>
      <div class="d-grid">
        <button class="btn btn-warning text-light fw-bold" @click="handleSubmitForm">
          Submit your information
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["isIntervieweeLogin"],
  data() {
    return {
      formTitle: "Apply for Jobs",
      isModifyTitle: false,
      cvFileName: "",
    };
  },
  methods: {
    handleModifyTitle() {
      this.isModifyTitle = !this.isModifyTitle;
    },
    handleSaveTitle() {
      this.isModifyTitle = !this.isModifyTitle;
    },
    handleCVFileUpload(e) {
      var filePath = e.target.value;
      var fileName = filePath.substring(filePath.lastIndexOf("\\") + 1);
      this.cvFileName = fileName;
    },
    handleSubmitForm() {
      if (this.isIntervieweeLogin) {
        var folderId = this.$route.query.folderId ?? 'UKN';
        alert("Gửi CV tới folder " + folderId + " thành công!")
      }
    },
  },
};
</script>

<style scoped>
.formApplyCV {
  width: 500px;
  padding: 35px;
  border-radius: 5px;
  border: 1px solid gainsboro;
  font-size: 20px;
  color: orange;
  background-color: rgb(248, 248, 150);
  box-shadow: rgba(50, 50, 93, 0.25) 0px 13px 27px -5px,
    rgba(0, 0, 0, 0.3) 0px 8px 16px -8px;
}

input {
  border-color: greenyellow;
  border-radius: 20px;
  box-shadow: rgba(0, 0, 0, 0.16) 0px 1px 4px;
}

#cvFileUploadLabel {
  cursor: pointer;
  background-color: orange;
  border: 2px solid orange;
  color: white;
  font-weight: bold;
  border-radius: 40px;
  text-align: center;
  width: 220px;
  padding: 10px;
  font-size: 16px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

#cvFileUploadLabel i {
  background-color: white;
  color: orange;
  font-weight: bold;
  padding: 6px;
  font-size: 12px;
  border-radius: 50%;
}

#cvFileUploadLabel:hover {
  background-color: white;
  color: orange;
}

#cvFileUploadLabel:hover i {
  background-color: orange;
  color: white;
}

#cvFileName {
  color: orange;
  font-weight: bold;
  font-size: 16px;
}

/* Chrome, Safari, Edge, Opera */
input::-webkit-outer-spin-button,
input::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}

/* Firefox */
input[type="number"] {
  -moz-appearance: textfield;
}
</style>
