import json
from pprint import pprint


def movie_info(movies, genres):
    movie_list = []
    for movie in movies:
                  
        genre_ids =  movie['genre_ids']
        def genre_ids_to_name(ids_list):
            name_list = []
            for ids in ids_list:

                 for genre in genres:
              
                    if ids == genre["id"]:
                        name_list.append(genre["name"])

            return name_list
      


        id =  movie['id']
        overview =  movie['overview']
        poster_path =  movie['poster_path']
        title =  movie['title']
        vote_average =  movie['vote_average']
        result = {'genre_names':genre_ids_to_name(genre_ids),'id':id,'overview':overview , 'poster_path':poster_path, 'title':title, 'vote_average':vote_average}
        movie_list.append(result)
    pprint(movie_list)

   
        
      
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))