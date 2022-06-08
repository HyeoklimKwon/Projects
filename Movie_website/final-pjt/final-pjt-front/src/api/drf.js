const HOST = 'http://localhost:8000/api/v1/'
const HOST2 = 'https://api.themoviedb.org/3/movie/'
const HOST3 = 'https://api.themoviedb.org/3/search/movie?query='

const ACCOUNTS = 'accounts/'
const MOVIES = 'movies/'
const REVIEWS = 'reviews/'
const ARTICLES = 'articles/'
const COMMENTS = 'comments/'
const RECOMMENDATIONS = 'recommendations'

export default {
  accounts: {
    login: () => HOST + ACCOUNTS + 'login/',
    logout: () => HOST + ACCOUNTS + 'logout/',
    signup: () => HOST + ACCOUNTS + 'signup/',
    // Token 으로 현재 user 판단
    currentUserInfo: () => HOST + ACCOUNTS + 'user/',
    // username으로 프로필 제공
    profile: username => HOST + ACCOUNTS + 'profile/' + username,
  },
  movies: {
    // /articles/
    movies: () => HOST + MOVIES,
    // /articles/1/
    movie: moviePk => HOST + MOVIES + `${moviePk}/`,
    reviews: moviePk => HOST + MOVIES + `${moviePk}/` + REVIEWS,
    recommendations: moviePk => HOST2 + `${moviePk}/` + RECOMMENDATIONS + "?api_key=87931dd6e8327ea04518e5e2a6836196&language=ko",
    search: value => HOST3 + `${value}&` + "api_key=87931dd6e8327ea04518e5e2a6836196&language=ko",
    review: (moviePk, reviewPk) =>
      HOST + MOVIES + `${moviePk}/` + REVIEWS + `${reviewPk}/`,
  },
  articles: {
    // /articles/
    articles: () => HOST + ARTICLES,
    // /articles/1/
    article: articlePk => HOST + ARTICLES + `${articlePk}/`,
    likeArticle: articlePk => HOST + ARTICLES + `${articlePk}/` + 'like/',
    comments: articlePk => HOST + ARTICLES + `${articlePk}/` + COMMENTS,
    comment: (articlePk, commentPk) =>
      HOST + ARTICLES + `${articlePk}/` + COMMENTS + `${commentPk}/`,
  },
}
