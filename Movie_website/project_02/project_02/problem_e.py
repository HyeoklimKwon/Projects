from unittest import result
import requests
from pprint import pprint


def credits(title):
    base_url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    params = {
    'api_key': '86be6a224df194a9a21faf6e63e1b00b',
    'region': 'KR',
    'language': 'ko',
    'query' : title
    }
    search_response = (requests.get(base_url+path, params= params).json()).get('results')
    if search_response != [] :
        for searched_movie in search_response :
            if searched_movie.get('title') == title :
                movie_id = searched_movie.get('id')

    
      
    else :
        return None

    path2 = f'/movie/{movie_id}/credits'

    params2 = {
    'api_key': '86be6a224df194a9a21faf6e63e1b00b',
    'region': 'KR',
    'language': 'ko',
    'query' : 'api_key=<<api_key>>&language=en-US',
    'movie_id' : int(f'{movie_id}')
    }

    credit_response = (requests.get(base_url+path2, params= params2).json())
    cast_response = credit_response.get('cast')
    crew_response = credit_response.get('crew')

    act_list = []
    direct_list = []

    for cast in cast_response :
        if cast.get('cast_id') < 10:
            act_list.append(cast.get('name'))
    
    for director in crew_response :
        if director.get('department') == 'Directing' :
            direct_list.append(director.get('name')) 
    
    result = {'cast' : act_list , 'crew' : direct_list}

    return result


    


if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화 id를 통해 영화 상세정보를 검색하여
    주연배우 목록(cast)과 제작진(crew).
    영화 id검색에 실패할 경우 None.
    """
    pprint(credits('기생충'))
    # => {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # => None
