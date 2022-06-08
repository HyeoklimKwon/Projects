import requests
from pprint import pprint



def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '86be6a224df194a9a21faf6e63e1b00b',
    'region': 'KR',
    'language': 'ko'
    }


    response = requests.get(base_url+path, params= params).json()
    return(len(response.get('results')))

if __name__ == '__main__':
    """
    popular 영화목록의 개수 출력.
    """
    print(popular_count())
    # => 20
