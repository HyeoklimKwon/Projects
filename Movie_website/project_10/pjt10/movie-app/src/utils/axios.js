import axios from "axios";

const request = axios.create({
  baseURL: "https://api.themoviedb.org/3/",
  params: {
    api_key: "86be6a224df194a9a21faf6e63e1b00b",
    language: "ko-KR",
  },
});

export const movieApi = {
  nowPlaying: () => request.get("movie/now_playing"),    
  movieDetail: (id) =>
    request.get(`movie/${id}`, {
      params: { append_to_response: "videos" },
    }),      
};
