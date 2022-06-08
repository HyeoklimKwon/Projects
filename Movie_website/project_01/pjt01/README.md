## Project01 TIL

### 1. 이중 for 문을 이용한 데이터 전처리 

```python
def movie_info(movie, genres):
      genre_ids =  movie['genre_ids']
      def genre_ids_to_name(ids_list):
          name_list = []
          for ids in ids_list:

            for genre in genres:
              
                if ids == genre["id"]:
                    name_list.append(genre["name"])

          return name_list
```

- problem b의 코드이다. movie에 있는 genre id 값들을 다시 genres 데이터에 비교해서 해당하는 값들에 대한 name을 다시 리스트로 변환하는 방법을 배웠다. 큰 movie 함수 라는 틀 안에 genre id to name 이라는 함수를 다시 생성하여 그 안에서 이중 for문을 이용해서 데이터를 처리하였다. 



### 2. 경로를 지정하여 해당되는 파일 현재 디렉토리에 사용

```python
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
```

- 모든 문제에 있었던 코드이다. 처음에는 이러한 코드들의 역할을 생각하지 못하고 지정된 함수 변수에 return을 넣어서 반환값을 보고 규칙을 이해하였다. 그렇다 보니 problem d,e 에서 현재 디렉토리가 아닌 다른 위치에 있는 파일들을 현재 디렉토리에 사용하는 상황에 막혔었다. 
- 결론적으로 말하자면 위의 코드들을 다시 유심히 관찰한 결과, 위에 코드가 data에 있는 movies.jason이라는 파일 UTF8 읽기 방식으로 읽은 파일을 movies_jason에 저장하고 이 movies_jason이라는 파일을 json.load라는 함수를 사용하여 리스트를 변환한 후 movies_list에 저장한다는 것을 깨달았다. 

```python
for movie in movies:
        movie_title = movie['title']
        movie_id = movie['id']
        movie_detail_json = open(f'data/movies/{movie_id}.json',encoding='UTF8')
        movie_detail = json.load(movie_detail_json)
```

- 위의 코드는 problem d를 푸는 함수 중간에 movie의 세부사항 정보 (다른 경로에 있는)를 읽기 위해 사용한 코드이다. 이를 이용하여 movie의 세부사항을 list로 변환하여 movie_detail에 저장하였고 

```python
    movie_dict = {'title' : movie_title , 'revenue' : movie_revenue}
        movie_revenue_list.append(movie_revenue)
        movie_list.append(movie_dict)
    for revenues in movie_list:
        reven = revenues['revenue']
        if reven == max(movie_revenue_list):
            pop_movie_title = revenues['title']
    return pop_movie_title
```

- 이를 영화별로 movie title과 같이 하나의 딕셔너리형식으로 만들어 저장한 후 ,  한데모아 list로 만들었다. 이후에 for문을 사용하여 가장 큰 revenue 값에 해당되는 영화 제목을 출력하게 하였다. 

