import requests
import json
from api_key import URLMaker


result = []
url = URLMaker.url
key = URLMaker.key
for page in range(1, 101):
    URL = f'{url}?api_key={key}&language=ko-Kr&page={page}'
    movies = requests.get(URL).json()

    for movie in movies['results']:
      if movie.get('release_date', '') and movie.get('overview', ''):
        fields = {
            'genres': movie['genre_ids'],
            'overview': movie['overview'],
            'popularity': movie['popularity'],
            'poster_path': movie['poster_path'],
            'release_date': movie['release_date'],
            'title': movie['title'],
            'vote_average': movie['vote_average'],
            'vote_count': movie['vote_count'],
        }

        data = {
            "pk": movie['id'],
            "model": "movies.movie",
            "fields": fields
        }

        result.append(data)

with open('movies.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False))

## 2. genre 정보

data = [
    {
      "id": 28,
      "name": "액션"
    },
    {
      "id": 12,
      "name": "모험"
    },
    {
      "id": 16,
      "name": "애니메이션"
    },
    {
      "id": 35,
      "name": "코미디"
    },
    {
      "id": 80,
      "name": "범죄"
    },
    {
      "id": 99,
      "name": "다큐멘터리"
    },
    {
      "id": 18,
      "name": "드라마"
    },
    {
      "id": 10751,
      "name": "가족"
    },
    {
      "id": 14,
      "name": "판타지"
    },
    {
      "id": 36,
      "name": "역사"
    },
    {
      "id": 27,
      "name": "공포"
    },
    {
      "id": 10402,
      "name": "음악"
    },
    {
      "id": 9648,
      "name": "미스터리"
    },
    {
      "id": 10749,
      "name": "로맨스"
    },
    {
      "id": 878,
      "name": "SF"
    },
    {
      "id": 10770,
      "name": "TV 영화"
    },
    {
      "id": 53,
      "name": "스릴러"
    },
    {
      "id": 10752,
      "name": "전쟁"
    },
    {
      "id": 37,
      "name": "서부"
    }
]

result = []

for genre in data:
    genre_dict = {
        "model" : "movies.genre",
        "pk" : genre.get("id"),
        "fields" : {
            "name" : genre.get("name")
        }
    }
    result.append(genre_dict)

with open('genres.json', 'w', encoding='UTF-8') as file:
    file.write(json.dumps(result, ensure_ascii=False))
