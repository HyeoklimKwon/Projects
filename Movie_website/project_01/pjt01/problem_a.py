import json
from pprint import pprint


def movie_info(movie):
      genre_ids =  movie['genre_ids']
      id =  movie['id']
      overview =  movie['overview']
      poster_path =  movie['poster_path']
      title =  movie['title']
      vote_average =  movie['vote_average']
      result = {'genre_ids':genre_ids,'id':id,'overview':overview , 'poster_path':poster_path, 'title':title, 'vote_average':vote_average}
      pprint(result)

      


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))