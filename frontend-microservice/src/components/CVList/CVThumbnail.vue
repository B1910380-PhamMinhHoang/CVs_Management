<template>
  <div class="p-3 col-sm-6 col-md-4 col-lg-3 mt-3" @click="seeDetailCV">
    <div class="cv-image">
      <span class="delete-icon float-right">X</span>
      <canvas :id="cv._id" class="w-100 h-100"></canvas>
    </div>
    <div class="cv-name">{{ cv.interviewerName }}</div>
  </div>
</template>

<script>
export default {
  props: ["cv"],
  methods: {
    seeDetailCV() {
      this.$router.push({ name: "cv", params: { cvId: this.cv._id } });
    },
  },
  mounted() {
    var idCV = this.cv._id;

    var pdfjsLib = window["pdfjs-dist/build/pdf"];
    pdfjsLib.GlobalWorkerOptions.workerSrc =
      "//mozilla.github.io/pdf.js/build/pdf.worker.js";

    pdfjsLib.getDocument("/pdf.pdf").promise.then(
      (pdf) => {
        pdf.getPage(1).then((page) => {
          var viewport = page.getViewport({ scale: 1 });
          var canvas = document.getElementById(idCV);
          var context = canvas.getContext("2d");
          canvas.height = viewport.width;
          canvas.width = viewport.height;
          page.render({
            canvasContext: context,
            viewport: viewport,
          });
        });
      },
      (error) => console.log(error)
    );
  },
};
</script>

<style scoped>
.cv-image {
  height: 300px;
  position: relative;
  cursor: pointer;
}

.cv-image .delete-icon {
  position: absolute;
  top: 5px;
  right: 10px;
  font-size: 25px;
  opacity: 0;
}

.cv-image img {
  width: 100%;
  height: 100%;
}

.cv-name {
  text-align: center;
  font-size: 25px;
  margin-top: 10px;
  font-weight: bold;
  padding: 5px;
}

.cv-image:hover canvas {
  opacity: 0.5;
}

.cv-image:hover .delete-icon {
  opacity: 1;
}
</style>
