<template>
  <div class="container-fluid">
    <div class="row">
      <div class="col-2 folderId">
        <i class="fa-solid fa-folder"></i> {{ folderId }}
      </div>
      <div class="col-7">
        <input
          type="text"
          class="form-control"
          id="searchInput"
          placeholder="Search CVs"
        />
      </div>
      <div class="col-3">
        <button class="btn w-100" id="searchBtn">
          <i class="fa-solid fa-magnifying-glass"></i>
          Search
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  props: ["folderId"],
};
</script>

<style scoped>
.folderId {
  font-size: 25px;
}

#searchBtn {
  cursor: pointer;
  background-color: rgb(24, 231, 24);
  color: whitesmoke;
  font-weight: bold;
  border-radius: 5px;
  text-align: center;
  width: 220px;
  font-size: 16px;
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

#searchBtn i {
  color: white;
  font-weight: bold;
  padding: 6px;
  font-size: 12px;
}

#searchBtn:hover {
  background-color: green;
}
</style>
