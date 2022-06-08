## Project02 TIL

### 1. 외부데이터에서 수집해서 원하는 결과 도출(TMDB) -이론

- 웹 스크래핑( 웹 크롤링)

  - query = "keyword" (찾고자 하는 대상)

  - 우리가 보는 웹은 '문서' 이다. (내가 원하는대로 바꿀 수 있음)

    ex)      요청(클라이언트 )     <===========>  응답(서버)

  - 위의 것을 파이썬으로 요청을 하고 받은 데이터를 파이썬으로 가공

  -  request 설치 : git bash(터미널창)에서 pip install requests

- 파이썬에서 정보 요청하는 법

  - 1. 주소 정리  

    ex) URL = 'https://naver/com'

  - 2. 요청

    ```python
    import requests
    response = requests.get(URL)
    print(response) # 200이 나왔다면 성공적으로 정보 수집
    
    resoponse = requests.get(URL).text
    print(response) => 코드를 볼 수 있다. 
    
    ```

    

- BeautifulSoup 사용

  ```python 
  from bs4 import BeautifulSoup 
  data = BeautifulSoup(response, 'html-parser') # html일때
  #이렇게 되면 클래스가 'str' => 'BeautifulSoup'으로 바뀜
  ```



- Json & API
  - API : 약속해놓은 정보 형태 (json()을 요청하면 json()을 주기로)
  - json : 리스트 안, 딕셔너리 형태로 정보들이 저장되어있는 형식의 데이터



### 2. 외부데이터에서 수집해서 원하는 결과 도출(TMDB) -코드

```python
def popular_count():
    base_url = 'https://api.themoviedb.org/3'
    path = '/movie/popular'
    params = {
    'api_key': '86be6a224df194a9a21faf6e63e1b00b',
    'region': 'KR',
    'language': 'ko'
    }

```

- 위와 같이 API정보를 받기 위해서는 위와 같이 url과 params를 미리 설정해주어서 접근이 가능하도록 해야한다.

```python
response = requests.get(base_url+path, params= params).json()
    return(len(response.get('results')))

```

- response 값을 json파일 형식으로 저장(할당)하기 위해서 .json()을 붙여주고 데이터를 처리한다.
- 여기서 return값으로 설정하면 뒤에 나오는 값 뒤에 None이 자동으로 삭제된다. None만 있을 경우 None 출력 

```python
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
```

- path2 처럼 입력 값이 필요한 경우 f-string 문법을 사용하여, 검색할 값을 임의로 입력해서 url에 붙일 수 있다. 

  

