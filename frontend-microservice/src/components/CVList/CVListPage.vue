<template>
  <div>
    <div class="searchBox m-5 p-3">
      <c-v-list-search-input :folderId="folderId" />
    </div>
    <div class="container-fluid p-0">
      <h1 class="pageTitle mx-5">Your CVs</h1>
      <div class="row m-5 mt-4 py-2 cvs">
        <div class="btn-group" role="group" id="cv-state-btn-group">
          <input
            type="radio"
            class="btn-check"
            name="btnradio"
            id="reviewing-cv"
            autocomplete="off"
            checked
          />
          <label
            class="btn btn-outline-success fw-bold"
            for="reviewing-cv"
            @click="isShowDoneReviewCV = false"
            >Reviewing</label
          >

          <input
            type="radio"
            class="btn-check"
            name="btnradio"
            id="done-review-cv"
            autocomplete="off"
          />
          <label
            class="btn btn-outline-success fw-bold"
            for="done-review-cv"
            @click="isShowDoneReviewCV = true"
            >Done review</label
          >
        </div>
        <div id="total-cv">Total: {{ cvsFiltered.length }} CVs</div>
        <c-v-thumbnail v-for="cv in cvsFiltered" :key="cv._id" :cv="cv" />
      </div>
    </div>
  </div>
</template>

<script>
import CVListSearchInput from "./CVListSearchInput.vue";
import CVThumbnail from "./CVThumbnail.vue";

export default {
  components: {
    CVListSearchInput,
    CVThumbnail,
  },
  created() {
    this.folderId = this.$route.params.folderId;
  },
  data() {
    return {
      folderId: "",
      cvs: [
        {
          _id: "cv1",
          interviewerName: "user 1",
          thumbnail: "/pikachu1.jpg",
          folderId: "a a a a a a a a a a",
          isDoneReview: true,
          extraInfo: {
            name: "User 1",
            phoneNumber: "1111111111",
          },
        },
        {
          _id: "cv2",
          interviewerName: "user 2",
          thumbnail: "/pikachu3.jpg",
          folderId: "b",
          isDoneReview: true,
          extraInfo: {
            name: "User 2",
            phoneNumber: "2222222222",
          },
        },
        {
          _id: "cv3",
          interviewerName: "user 3",
          thumbnail: "/pikachu2.jpeg",
          folderId: "b",
          isDoneReview: false,
          extraInfo: {
            name: "User 3",
            phoneNumber: "3333333333",
          },
        },
        {
          _id: "cv4",
          interviewerName: "user 4",
          thumbnail: "/pikachu1.jpg",
          folderId: "a a a a a a a a a a",
          isDoneReview: true,
          extraInfo: {
            name: "User 4",
            phoneNumber: "4444444444",
          },
        },
        {
          _id: "cv5",
          interviewerName: "user 5",
          thumbnail: "/pikachu3.jpg",
          folderId: "UKN",
          isDoneReview: false,
          extraInfo: {
            name: "User 5",
            phoneNumber: "5555555555",
          },
        },
        {
          _id: "cv6",
          interviewerName: "user 6",
          thumbnail: "/pikachu1.jpg",
          folderId: "a a a a a a a a a a",
          isDoneReview: true,
          extraInfo: {
            name: "User 6",
            phoneNumber: "6666666666",
          },
        },
        {
          _id: "cv7",
          interviewerName: "user 7",
          thumbnail: "/pikachu3.jpg",
          folderId: "b",
          isDoneReview: true,
          extraInfo: {
            name: "User 7",
            phoneNumber: "7777777777",
          },
        },
        {
          _id: "cv8",
          interviewerName: "user 8",
          thumbnail: "/pikachu2.jpeg",
          folderId: "b",
          isDoneReview: false,
          extraInfo: {
            name: "User 8",
            phoneNumber: "8888888888",
          },
        },
        {
          _id: "cv9",
          interviewerName: "user 9",
          thumbnail: "/pikachu1.jpg",
          folderId: "a a a a a a a a a a",
          isDoneReview: true,
          extraInfo: {
            name: "User 9",
            phoneNumber: "9999999999",
          },
        },
        {
          _id: "cv10",
          interviewerName: "user 10",
          thumbnail: "/pikachu1.jpg",
          folderId: "c",
          isDoneReview: false,
          extraInfo: {
            name: "User 10",
            phoneNumber: "1010101010",
          },
        },
      ],
      isShowDoneReviewCV: false,
    };
  },
  computed: {
    cvsFiltered() {
      return this.cvs.filter(
        (cv) =>
          cv.folderId == this.folderId &&
          cv.isDoneReview == this.isShowDoneReviewCV
      );
    },
  },
};
</script>

<style scoped>
.pageTitle {
  font-size: 50px;
}

.searchBox {
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

.cvs {
  box-shadow: rgba(0, 0, 0, 0.24) 0px 3px 8px;
}

#total-cv {
  font-size: 20px;
  margin: 20px;
}

#cv-state-btn-group {
  width: 80%;
  margin: 20px auto 10px;
}

#cv-state-btn-group label {
  border-radius: 0;
}
</style>
