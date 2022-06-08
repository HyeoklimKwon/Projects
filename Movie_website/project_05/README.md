## Project05 TIL

### 1. 오류 

 (Django의 기본 개념은 쉽게 이해하였지만 막상 만들기 시작하면, 오류가 너무 많이 났다. )

```django
1) migrate를 안할 경우 operational Error가 발생한다.
```

```django
2) model를 만들때 뒤에 ()표시를 안해주면 정상적인 데이터 작동이 불가능하여 다시 새로운 model를 만들어야 한다. 
```



### 2.  select를 이용한 선택창 만들기

```html
<div class="mb-3">
        <label for="genre" class="form-label">GENRE</label>
        <select id = "genre" class="form-select" aria-label="Default select example" name= "genre">
            <option selected>장르를 선택해주세요</option>
            <option value="코미디">코미디</option>
            <option value="액션">액션</option>
            <option value="로맨스코미디">로맨스코미디</option>
          </select>
```

위와 같이 직접 입력하는 것이 아닌 기존 선택창을 만들때 bootstrap에 있는 selec 코드를 가져와서 만들어준다. 

핵심적인 부분 

1) name id for 해당 변수로 일치시켜주기
2)  value 값에 1,2,3 기본 값이 아닌 정확히 선택한 값들로 바꿔서 movie.genre에 정확히 담아준다.

```python

def create(request):
    title = request.POST.get('title')
    audience = request.POST.get('audience')
    release_date = request.POST.get('release_date')
    genre = request.POST.get('genre')
    score = request.POST.get('score')
    poster_url = request.POST.get('poster_url')
    description = request.POST.get('description')
    
    movie = Movie()
    movie.title = title
    movie.audience = audience
    movie.release_date = release_date
    movie.genre = genre
    movie.score = score
    movie.poster_url = poster_url
    movie.description = description  
    movie.save()
```

그렇게 해서 받은 genre 값을 모델 클래스 Movie에 생성된 객체 movie.genre값에 할당을 해준다. 

```html
<div class="mb-3">
            <label for="genre" class="form-label">GENRE</label>
            <input type="text" name="genre" id="genre" class="form-control" value = "{{ movie.genre}}">
```

그 후 edit 페이지에서는 선택창에서 없는 값이 있을 수 있기 떄문에 자유롭게 바꿀수 있도록 바꿨다. 



### 3. Date 값 다루기 

date 값을 다루면서 오류에 부딪혔던 부분은 edit로 전환당시 기존에 썼던 값이 date에 저장이 되지 않는다는 점이었다. 다른 값들 경우 value 값을 {{ movie.variable}} 형식으로 주면되지만, date의 값경우 그렇지 않기 떄문에 한번더 변환해주는 함수를 사용하여야 한다. 

```html
<div class="mb-3">
            <label for="release_date" class="form-label">RELEASE_DATE</label>
            <input type="date" name="release_date" id="release_date" class="form-control" value="{{ movie.release_date|date:'Y-m-d' }}">
        </div>
```

위의 코드와 같이 value="{{ movie.release_date|date:'Y-m-d' }}" 를 사용하여 기존에 있던 값을 year month date로 구분시켜주고 그 값을 기존 value로 넣어준다. 