<template>
  <div class="wrapper">
    <div
      class="interviewer-detail-button"
      data-bs-toggle="modal"
      data-bs-target="#interviewer-detail-modal"
    >
      More detail
    </div>
    <div
      class="modal fade"
      id="interviewer-detail-modal"
      tabindex="100"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered">
        <div class="modal-content p-2">
          <div class="modal-body">
            <div class="row">
              <div class="main-title col-4">CV's detail</div>
              <div class="btn-group col-6 h-75 mt-2" role="group" id="cv-state-btn-group">
                <input
                  type="radio"
                  class="btn-check"
                  name="btnradio"
                  id="reviewing-cv"
                  autocomplete="off"
                  :checked="!isShowDoneReviewCV"
                />
                <label class="btn btn-outline-info fw-bold" for="reviewing-cv"
                  >Reviewing</label
                >
                <input
                  type="radio"
                  class="btn-check"
                  name="btnradio"
                  id="done-review-cv"
                  autocomplete="off"
                  :checked="isShowDoneReviewCV"
                />
                <label class="btn btn-outline-info fw-bold" for="done-review-cv"
                  >Done review</label
                >
              </div>
              <div class="col-2 x-icon" data-bs-dismiss="modal">X</div>
            </div>
            <h4 class="title">
              <i class="fa-solid fa-diamond"></i>
              Interviewer's information:
            </h4>
            <table>
              <tr v-for="(value, key) in moreDetail" :key="key">
                <th>{{ key }}:</th>
                <td>{{ value }}</td>
              </tr>
              <tr>
                <th>Name:</th>
                <td>dsad dsa dsa a</td>
              </tr>
              <tr>
                <th>Name ds dsd :</th>
                <td>dsad dsa dsa a</td>
              </tr>
            </table>
            <h4 class="title">
              <i class="fa-solid fa-diamond"></i>
              Recommended Jobs:
            </h4>
            ...
          </div>
        </div>
      </div>
    </div>
    <div class="interviewer-detail" v-if="isShowDetail">jk</div>
  </div>
</template>

<script>
export default {
  props: ["cvDetail"],
  data() {
    return {
      isShowDoneReviewCV: this.cvDetail.isDoneReview,
      moreDetail: this.cvDetail.extraInfo,
    };
  },
};
</script>

<style scoped>
.wrapper {
  position: fixed;
  bottom: 40px;
  right: 40px;
}

.interviewer-detail-button {
  border-radius: 50%;
  width: 80px;
  height: 80px;
  text-align: center;
  align-items: center;
  background-color: gold;
  cursor: pointer;
  display: flex;
  align-content: center;
  color: brown;
  font-weight: bold;
}

.interviewer-detail-button:hover {
  background-color: yellow;
  color: brown;
}

.modal-dialog {
  max-width: 800px;
}

.main-title {
  font-size: 35px;
  color: blue;
  font-weight: bold;
}

.x-icon {
  font-size: 35px;
  text-align: right;
  cursor: pointer;
  padding-right: 20px;
}

.x-icon:hover {
  font-weight: bold;
  color: brown;
}

.fa-diamond {
  font-size: 18px;
}

td {
  padding-left: 15px;
}

.title {
  margin-top: 20px;
}

textarea:focus,
input:focus {
  border-color: none;
  box-shadow: none;
  outline: 0 none;
}
</style>
