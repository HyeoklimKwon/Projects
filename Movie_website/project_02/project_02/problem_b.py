import requests
from pprint import pprint


def vote_average_movies():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '86be6a224df194a9a21faf6e63e1b00b',
    'region': 'KR',
    'language': 'ko'
    }
    response = (requests.get(base_url+path, params= params).json()).get('results')
    vote_movie_list = []
    for movie_data in response :
        if movie_data.get('vote_average') >= 8 :
            vote_movie_list.append(movie_data)
    return vote_movie_list


if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 출력.
    """
    pprint(vote_average_movies())
    # => 영화정보 순서대로 출력
