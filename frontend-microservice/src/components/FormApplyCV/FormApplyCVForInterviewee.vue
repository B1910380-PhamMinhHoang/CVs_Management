<template>
  <div id="formApplyCVForInterviewee">
    <h1>Form for interviewee</h1>
    <form-apply-c-v :isIntervieweeLogin="true" />
  </div>
</template>

<script>
import FormApplyCV from "./FormApplyCV.vue";

export default {
  components: {
    FormApplyCV,
  },
  created() {
    this.$emit("intervieweeLogin");
  },
  data() {
    return {
      
    };
  }
};
</script>

<style scoped>
#formApplyCVForInterviewee {
    background-color: lightgreen;
}

h1 {
  text-align: center;
  margin-top: 20px;
  font-size: 50px;
  color: white;
}
</style>
