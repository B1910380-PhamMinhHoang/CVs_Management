<template>
  <div
    class="modal fade"
    id="addCVFolderModal"
    tabindex="-1"
    aria-labelledby="addCVFolderModal"
    aria-hidden="true"
  >
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-body text-center p-4">
          <h1 class="modal-title fs-5">Add A Folder</h1>
          <div>
            <div class="mb-3 row">
              <label for="idInput" class="col-sm-2 col-form-label">Id:</label>
              <div class="col-sm-10">
                <input type="text" class="form-control" id="idInput" />
              </div>
            </div>
            <div class="mb-3 row">
              <label for="nameInput" class="col-sm-2 col-form-label"
                >Name:</label
              >
              <div class="col-sm-10">
                <input type="text" class="form-control" id="nameInput" />
              </div>
            </div>
          </div>
          <button id="buttonAdd">Add</button>
          <button id="buttonClose" data-bs-dismiss="modal" aria-label="Close">
            Close
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
#addCVFolderModal {
  font-size: 18px;
  font-weight: bold;
}

#addCVFolderModal .modal-body {
  background-color: lightyellow;
}

#buttonAdd,
#buttonClose {
  width: 100px;
  margin: 0 10px;
  border: none;
  border-radius: 10px;
  padding: 5px 0;
  font-weight: bold;
  color: white;
}

#buttonAdd {
  background-color: yellowgreen;
}

#buttonClose {
  background-color: orange;
}

#buttonAdd:hover {
  background-color: green;
}

#buttonClose:hover {
  background-color: goldenrod;
}
</style>
