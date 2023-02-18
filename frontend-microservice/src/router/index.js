import { createWebHistory, createRouter } from "vue-router";
import CVFolderPage from "./../components/CVFolder/CVFolderPage.vue";
import CVListPage from "./../components/CVList/CVListPage.vue";
import CVDetailPage from "./../components/CVDetail/CVDetailPage.vue";
import FormApplyCV from "./../components/FormApplyCV/FormApplyCV.vue";
import FormApplyCVForInterviewee from "./../components/FormApplyCV/FormApplyCVForInterviewee.vue";

const routes = [
  {
    path: "/",
    name: "folders",
    component: CVFolderPage,
  },
  {
    path: "/cvs/:folderId",
    name: "cvs",
    component: CVListPage,
    params: true,
  },
  {
    path: "/cv/:cvId",
    name: "cv",
    component: CVDetailPage,
    params: true,
  },
  {
    path: "/form/applyCV",
    name: "applyCVForm",
    component: FormApplyCV,
  },
  {
    path: "/applyCV",
    name: "applyCVFormForInterviewee",
    component: FormApplyCVForInterviewee,
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

export default router;
