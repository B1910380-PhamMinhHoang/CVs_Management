<template>
  <div>
    <embed
      src="/pdf.pdf"
      type="application/pdf"
      scrolling="auto"
      width="100%"
      class="p-0 m-0"
    />
    <interviewer-detail-button :cvDetail="cvDetail" />
  </div>
</template>

<script>
import InterviewerDetailButton from "./InterviewerDetailButton.vue";

export default {
  components: {
    InterviewerDetailButton,
  },
  created() {
    this.cvId = this.$route.params.cvId;
  },
  data() {
    return {
      cvId: "",
      cvs: [
        {
          _id: "cv1",
          interviewerName: "user 1",
          thumbnail: "/pikachu1.jpg",
          folderId: "a a a a a a a a a a",
          isDoneReview: true,
          extraInfo: {
            Name: "User 1",
            "Phone number": "1111111111",
          },
        },
        {
          _id: "cv2",
          interviewerName: "user 2",
          thumbnail: "/pikachu3.jpg",
          folderId: "b",
          isDoneReview: true,
          extraInfo: {
            Name: "User 2",
            "Phone number": "2222222222",
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
            "Phone number": "3333333333",
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
            "Phone number": "4444444444",
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
            "Phone number": "5555555555",
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
            "Phone number": "6666666666",
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
            "Phone number": "7777777777",
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
            "Phone number": "8888888888",
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
            "Phone number": "9999999999",
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
            "Phone number": "1010101010",
          },
        },
      ],
    };
  },
  computed: {
    cvDetail() {
      var cv = this.cvs.filter((cv) => cv._id == this.cvId);
      return cv ? cv[0] : null;
    },
  },
};
</script>

<style scoped>
embed {
  height: 99%;
}
</style>
