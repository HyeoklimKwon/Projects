import requests
from pprint import pprint


def recommendation(title):
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
    
    path2 = f'/movie/{movie_id}/recommendations'

    recommend_response = (requests.get(base_url+path2, params= params).json()).get('results')
    recommend_list = []
    for recommend_movie in recommend_response :
        recommend_list.append(recommend_movie.get('title'))



    return (recommend_list)
                
     

if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면
    해당 영화의 id를 기반으로 추천 영화 목록 구성.
    추천 영화가 없을 경우 [].
    영화 id검색에 실패할 경우 None.
    """
    pprint(recommendation('기생충'))
    # ['조커', '조조 래빗', '1917', ..., '토이 스토리 4', '스파이더맨: 파 프롬 홈']
    pprint(recommendation('그래비티'))
    # []  => 추천 영화 없음
    pprint(recommendation('검색할 수 없는 영화'))
    # => None
