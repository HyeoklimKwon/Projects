// 기본 url
// const HOST = process.env.VUE_APP_API_URL + "/api/v1";
const HOST = "https://i7b209.p.ssafy.io/api/v1/";

// ===================================
// 세부 url
const ACCOUNTS = "accounts/";
const CATEGORYS = "categorys/";
const STORY = "stories/";
const COMMENT = "comment/";
const REVIEW = "reviews/";
const STORE = "store/";
const CREW = "crews/";
const NOTIFICATION = "notifications/";
const SCHEDULE = "schedule/";
// const CHAT = 'chat/'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + "login/",
    kakaoLogin: () => HOST + ACCOUNTS + "kakao/",
    logout: () => HOST + ACCOUNTS + "logout/",
    signup: () => HOST + ACCOUNTS + "signup/",
    emailCheck: () => HOST + ACCOUNTS + "unique/email/",
    nicknameCheck: () => HOST + ACCOUNTS + "unique/nickname/",
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + "user/",
    // username으로 프로필 제공
    profile: (username) => HOST + ACCOUNTS + "profile/" + username,
    myInfo: (user_pk) => HOST + ACCOUNTS + user_pk + "/",
    searchallusers: () => HOST + ACCOUNTS + "users/",
  },

  crew: {
    crew: () => HOST + CREW,
    crewInfo: (crew_pk) => HOST + CREW + crew_pk + "/",
    article: (crew_article_pk) => HOST + CREW + "article/edit/" + crew_article_pk + "/",
    inviteuser: (crew_pk, user_pk) => HOST + CREW + "invite/" + crew_pk + "/" + user_pk + "/",
    articles: (crew_pk) => HOST + CREW + "article/" + crew_pk + "/",
    members: (crew_pk) => HOST + CREW + "user/" + crew_pk + "/",
    sign: (crew_pk) => HOST + CREW + "sign/" + crew_pk + "/",
    invitelist: (crew_pk, type) => HOST + CREW + "invitelist/" + crew_pk + "/?type=" + type,
    accept: (crew_pk, user_pk) => HOST + CREW + "accept_user/" + crew_pk + "/" + user_pk + "/",
    deny: (crew_pk, user_pk) => HOST + CREW + "deny_user/" + crew_pk + "/" + user_pk + "/",
    leave: (crew_pk) => HOST + CREW + "leave/" + crew_pk + "/",
    comment: (crew_article_pk) => HOST + CREW + "comment/" + crew_article_pk + "/",
    commentUpdate: (crew_comment_pk) => HOST + CREW + "comment/update/" + crew_comment_pk + "/",

    // myCrew: (user_pk) => HOST + CREW + user_pk + "/",
    acceptcrew: (crew_pk) => HOST + CREW + "accept_crew/" + crew_pk + "/",
    refusecrew: (crew_pk) => HOST + CREW + "deny_crew/" + crew_pk + "/",
    registercrewschedule: (crew_pk) => HOST + CREW + SCHEDULE + crew_pk + "/",
    getworklist: (crew_pk,date) => HOST + CREW + SCHEDULE + "work/" + crew_pk +"/"+ date + "/"
  },
  categorys: {
    job: () => HOST + CATEGORYS + "job/",
    region: () => HOST + CATEGORYS + "region/",
  },
  story: {
    host: () => HOST,
    story: () => HOST + STORY,
    hashtag: () => HOST + STORY + "hashtag/filter/",
    detail: (story_pk) => HOST + STORY + story_pk + "/",
    like: (story_pk) => HOST + STORY + "like/" + story_pk + "/",
    comment: (story_pk) => HOST + STORY + COMMENT + story_pk + "/",
    commentChange: (comment_pk) => HOST + STORY + COMMENT + "ud/" + comment_pk + "/",
    myStory: (user_pk) => HOST + STORY + "mystory/" + user_pk + "/",
  },
  review: {
    store: () => HOST + REVIEW + STORE,
    review: (store_pk) => HOST + REVIEW + store_pk + "/",
    reviewDetail: (review_pk) => HOST + REVIEW + "detail/" + review_pk + "/",
    like: (review_pk) => HOST + REVIEW + "like/" + review_pk + "/",
  },
  profile: {
    updateMyInfo: (user_pk) => HOST + ACCOUNTS + user_pk + "/",
    updateMyPW: (user_pk) => HOST + ACCOUNTS + "change_password/" + user_pk + "/",
    myFollow: (user_pk) => HOST + ACCOUNTS + "followlist/" + user_pk + "/",
    myStory: (user_pk) => HOST + STORY + "mystory/" + user_pk + "/",
    myReview: (user_pk) => HOST + ACCOUNTS + "review/" + user_pk + "/",
    myCrew: (user_pk) => HOST + ACCOUNTS + "crew/" + user_pk + "/",
    myInfo: (user_pk) => HOST + ACCOUNTS + user_pk + "/",
    follow: (user_pk) => HOST + ACCOUNTS + "follow/" + user_pk + "/",
    setBlackList: () => HOST + "blacklist/",
  },

  notification: {
    getnotifications: () => HOST + NOTIFICATION,
    getinvitedcrewlist: () => HOST + CREW + "signlist/?type=invite" ,
    deletenotification: (notification_pk) => HOST + NOTIFICATION + notification_pk,
    makeviewtrue: (notification_pk) => HOST + NOTIFICATION + notification_pk,
  },
};
