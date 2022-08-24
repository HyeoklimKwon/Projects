import { createRouter, createWebHistory } from "vue-router";
import Home from "@/pages/home/HomeView.vue";
import Chat from "@/pages/chat/ChatView.vue";
import MyProfile from "@/pages/profile/MyProfileView.vue";
import Login from "@/pages/account/LoginView.vue";
import KakaoLogin from "@/pages/account/KakaoLoginView.vue";
import Signup from "@/pages/account/signup/SignupView.vue";
import SignupChoice from "@/pages/account/signup/FirstSignupView.vue";
import SignupForm from "@/pages/account/signup/SecondSignupView.vue";
import SignupCategory from "@/pages/account/signup/ThirdSignupView.vue";

import Story from "@/pages/story/StoryView.vue";
import StoryFollow from "@/pages/story/StoryFollowView.vue";
import StoryMain from "@/pages/story/StoryMain.vue";
import StoryForm from "@/pages/story/StoryForm.vue";
import StoryDetailView from "@/pages/story/StoryDetailView.vue";

import Crew from "@/pages/crew/CrewView.vue";

import ReviewMain from "@/pages/review/ReviewMain.vue";
import ReviewView from "@/pages/review/ReviewView.vue";
import ReviewForm from "@/pages/review/ReviewForm.vue";
import ReviewDetail from "@/pages/review/ReviewDetail.vue";
import ReviewCommentDetail from "@/pages/review/ReviewCommentDetail.vue";
import Chatroom from "@/pages/chat/ChatroomView.vue";
import SearchCrewUsers from "@/pages/crew/SearchCrewUsersView.vue";
import ProfileMain from "@/pages/profile/ProfileMainView.vue";
import UpdateUserInfo from "@/pages/profile/UpdateUserInfoView.vue";
import FollowList from "@/pages/profile/FollowListView.vue";
import MyStory from "@/pages/profile/MyStoryView.vue";
import SearchAllUsers from "@/pages/crew/SearchAllUsersView.vue";
import InvitedCrew from "@/pages/profile/InvitedCrewView.vue";
import ReviewList from "@/pages/profile/ReviewListView.vue";
import CrewList from "@/pages/profile/CrewListView.vue";
import MyInfo from "@/pages/profile/MyInfoView.vue";
import UserProfile from "@/pages/profile/UserProfileView.vue";
import SetBlackList from "@/pages/profile/BlackListView.vue";
import DeleteAccount from "@/pages/profile/DeleteAccountView.vue";
import Notification from "@/pages/notification/NotificationView.vue";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/",
      name: "home",
      component: () => import("@/pages/MainLoadingView.vue"),
    },
    {
      path: "/login",
      name: "login",
      component: Login,
    },
    {
      path: "/kakao",
      name: "kakao",
      component: KakaoLogin,
    },
    {
      path: "/signup",
      name: "signup",
      component: Signup,
      redirect: "/signup/1",
      children: [
        {
          path: "1",
          name: "choice",
          component: SignupChoice,
        },
        {
          path: "2",
          name: "form",
          component: SignupForm,
        },
        {
          path: "3",
          name: "category",
          component: SignupCategory,
        },
      ],
    },
    {
      path: "/story",
      name: "",
      component: StoryMain,
      children: [
        {
          path: "",
          name: "story",
          component: Story,
        },
        {
          path: "follow",
          name: "followStory",
          component: StoryFollow,
        },
        {
          path: "create",
          name: "createStory",
          component: StoryForm,
        },
        {
          path: ":story_pk",
          name: "detailStory",
          component: StoryDetailView,
        },
      ],
    },

    {
      path: "/crew",
      name: "crew",
      redirect: "/crew/list",
      component: Crew,
      children: [
        {
          path: "regist",
          name: "crewregistview",
          redirect: { name: "crewregist" },
          component: () => import("@/components/crew/manage/regist/CrewRegistView.vue"),
          children: [
            {
              path: "",
              name: "crewregist",
              component: () => import("@/components/crew/manage/regist/CrewRegistInput.vue"),
            },
          ],
        },
        {
          path: "list",
          name: "crewlist",
          component: () => import("@/components/crew/list/CrewListView.vue"),
          children: [
            {
              path: "alllist",
              name: "allcrewlist",
              component: () => import("@/components/crew/list/CrewListAll.vue"),
            },
            {
              path: "mylist",
              name: "mycrewlist",
              component: () => import("@/components/crew/list/CrewListMy.vue"),
            },
          ],
        },
        {
          path: "search",
          name: "crewsearch",
          component: () => import("@/components/crew/list/CrewListSearch.vue"),
        },
        {
          path: "modify/:crew_pk",
          name: "crewmodify",
          component: () => import("@/components/crew/manage/CrewModify.vue"),
        },
        {
          path: "delete/:crew_pk",
          name: "crewdelete",
          component: () => import("@/components/crew/manage/CrewDelete.vue"),
        },
        {
          path: "detail/:crew_pk",
          name: "crewdetail",
          component: () => import("@/components/crew/manage/CrewDetail.vue"),
        },
        {
          path: "leave/:crew_pk",
          name: "crewleave",
          component: () => import("@/components/crew/member/CrewMemberLeave.vue"),
        },
        {
          path: "nm/:crew_pk",
          name: "crewboardnonmember",
          component: () => import("@/components/crew/manage/CrewBoardNonMember.vue"),
        },
        {
          path: "m/:crew_pk",
          name: "crewboardmember",
          component: () => import("@/components/crew/manage/CrewBoardMember.vue"),
          
        },
        {
          path: "article/:crew_pk",
          name: "article",
          component: () => import("@/components/crew/article/ArticleListView.vue"),
          children: [
            {
              path: "",
              name: "articlelist",
              component: () => import("@/components/crew/article/ArticleList.vue"),
            },
            {
              path: ":crew_article_pk",
              name: "articlemodify",
              component: () => import("@/components/crew/article/ArticleModify.vue"),
            },
            {
              path: ":crew_article_pk",
              name: "articledelete",
              component: () => import("@/components/crew/article/ArticleDelete.vue"),
            },
            
            // {
            //   path: "crewmember",
            //   name: "crewmember",
            //   component: () =>
            //     import("@/components/crew/crewmember/CrewMemberView.vue"),
            // },
          ],
        },
        {
          path: "article/detail/:crew_article_pk",
          name: "articledetail",
          component: () => import("@/components/crew/article/ArticleDetail.vue"),
        },
        {
          path: "regist/:crew_pk",
          name: "articleregist",
          component: () => import("@/components/crew/article/ArticleRegist.vue"),
        },

        {
          path: "user/:crew_pk",
          name: "crewmemberlist",
          component: () => import("@/components/crew/member/CrewMemberList.vue"),
        },
        {
          path: "request",
          name: "crewmemberrequestlist",
          component: () => import("@/components/crew/member/CrewMemberRequestList.vue"),
        },
      ],
    },
    {
      path: "/review",
      name: "",
      component: ReviewMain,
      children: [
        {
          path: "",
          name: "review",
          component: ReviewView,
        },
        {
          path: "create",
          name: "createReview",
          component: ReviewForm,
        },
        {
          path: ":store_pk/:store_name",
          name: "detailReview",
          component: ReviewDetail,
        },
        {
          path: ":store_pk/:store_name/:review_pk",
          name: "detailComment",
          component: ReviewCommentDetail,
        },
      ],
    },
    {
      path: "/chat/:from_userpk/:from_usernickname",
      name: "chat",
      component: Chat,
    },
    {
      path: "/profile",
      name: "",
      component: ProfileMain,
      children: [
        {
          path: "",
          name: "Profile",
          component: MyProfile,
        },
        {
          path: ":user_pk/update",
          name: "updateInfo",
          component: UpdateUserInfo,
        },
        {
          path: ":user_pk/updatePassword",
          name: "updatePassword",
          component: () => import("@/pages/profile/UpdatePasswordView.vue"),
        },
        {
          path: ":user_pk/:followType",
          name: "followList",
          component: FollowList,
        },
        {
          path: ":user_pk/mystory",
          name: "mystory",
          component: MyStory,
        },
        {
          path: ":user_pk/review",
          name: "reviewList",
          component: ReviewList,
        },
        {
          path: ":user_pk/crew",
          name: "crewList",
          component: CrewList,
        },
        {
          path: ":user_pk/myinfo",
          name: "myinfo",
          component: MyInfo,
        },
        {
          path: ":user_pk/delete",
          name: "deleteAccount",
          component: DeleteAccount,
        },
        {
          path: ":user_pk",
          name: "userProfile",
          component: UserProfile,
        },
        {
          path: "blacklist/:user_pk",
          name: "setBlackList",
          component: SetBlackList,
        },
      ],
    },
    {
      path: "/chatroom",
      name: "chatroom",
      component: Chatroom,
    },
    {
      path: "/searchusers/:crew_pk",
      name: "searchcrewusers",
      component: SearchCrewUsers,
    },
    {
      path: "/searchusers",
      name: "searchallusers",
      component: SearchAllUsers,
    },
    {
      path: "/invitedcrewlist",
      name: "invitedcrewlist",
      component: InvitedCrew,
    },
    {
      path: "/notifications",
      name: "notifications",
      component: Notification,
    },
    {
      path: "/crew/schedule/:crew_pk",
      name: "schedule",
      component: () => import("@/components/crew/schedule/ScheduleView.vue"),
    },
    {
      path: "/crew/scheduleregister/:crew_pk",
      name: "scheduleregister",
      component: () => import("@/components/crew/schedule/ScheduleRegisterView.vue"),
    },
  ],
});

export default router;
