import requests
from pprint import pprint


def ranking():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '86be6a224df194a9a21faf6e63e1b00b',
    'region': 'KR',
    'language': 'ko'
    }
    response = (requests.get(base_url+path, params= params).json()).get('results')
    #return sorted(response, key =lambda k : k['vote_average'])
    for j in range(len(response)) :
        k = len(response) - j
        for i in range(1,k) :
            if response[i-1].get('vote_average') <= response[i].get('vote_average'):
                temp = response[i-1]
                response[i-1] = response[i]
                response[i] = temp
    return response[0:5]

    

if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화.
    """
    pprint(ranking())
    # => 영화정보 순서대로 출력
