## Project4 TIL

*개인적인 체감으로 교육생 스스로 터득하면서 나가야할 점이 많았다. 기존의 프로젝트들이 수월했던것만큼 나름 어려운 편의 프로젝트였다고 생각한다.

### 복습하기

- 기존의 프로젝트들은 이번 프로젝트를 하기 위한 연습 과정이었다고 느껴짐. 이번 프로젝트를 풀기 위해 기본 개념들을 다시 복습하였다. 

```python
def recommendations(request):
    base_url = 'https://api.themoviedb.org/3'
    #api 정보 요청을 위해서 기존 url를 만든다. 
    params = {
    'api_key': '86be6a224df194a9a21faf6e63e1b00b',
    'region': 'KR',
    'language': 'ko'
    }
    path2 = f'/movie/278/recommendations'
	
    recommend_response = (requests.get(base_url+path2, params= params).json()).get('results')
    random_choice = random.choice(recommend_response)
    poster_path = random_choice.get('poster_path')
    # 이미지 주소를 검색하기 위해서 path와 기존 찾아볼 수 있는 주소를 합하여서 address라는 변수를 하나 더 만들어준다. 
    address = ('https://image.tmdb.org/t/p/w500'+poster_path)
    overview = random_choice.get('overview')
    vote = round(random_choice.get('vote_average'),1)
    title = random_choice.get('title')
    date = random_choice.get('release_date')
    context = {
           'address' : address,
           'overview': overview,
           'vote' : vote, 
           'title' : title,
           'date' : date,
        }

```

- api 요청하는 법을 잊고 있었지만 이번 프로젝트를 하면서 다시 복습하게 되는 계기가 되었다.

```python
{% block content %}
<h1 class="d-flex justify-content-center my-5 fw-bold" >쇼생크 탈출과 비슷한 영화 추천받기</h1>
<br>
<div class = "d-flex justify-content-center">
<div class="card mb-3" style="max-width: 75%;">
        <div class="row g-0">
          <div class="col-md-6">
            <img src= {{ address }} class="img-fluid rounded-start" alt="img">
          </div>
          <div class="col-md-6">
            <div class="card-body">
              <h5 class="card-title">{{ title }}
                <button type="button" class="btn btn-success">{{ vote }}</button>
              </h5>
```

- 그리드 사용법 익히기 d-flex 로 justify-content-center 로 가운데 정렬을 해주고 my-5 마진을 준다. 
- 그런다음 각 창의 크기에 따라 바뀌어야 하기 떄문에 md이상일때는 각각 6씩 즉 반반만 차지하게 해주고 그 이후는 설정을 해주지 않음으로서 하나만 뜨게 해준다. 

```html
{% block modal %}
<div class="modal fade" id="productModal-1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" >
  <div class="modal-dialog"  style="max-width: 100%; width: auto; display: table;" >
      # 위와 같은 설정을 해주지 않으면 사진이 짤리는 상황이 발생하게 된다. 
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
          <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
              <div class="carousel-inner">
                <div class="carousel-item active">
                  <img src="https://via.placeholder.com/840x600.jpg" alt="840 * 600 size image">
                    #placeholder을 통해 빈이미지를 생성한다. 
         (하략)

{% endblock modal %}
```

- 가장 어려운 점을 겪었던 것은 위처럼 modal 블록을 따로 설정해주지 않을 경우 top 버튼이 modal창까지 따라온다는 점이다. 따라서 modal 블록을 따로 설정해준다음, top (footer)와 분리를 시켜서 modal 창이 뜰때 top 버튼이 자동으로 사라지게 만들었다. 

- style에서 width를 auto로 설정해주지 않으면 modal창이 열릴떄, 그림이 짤려서 나오게 된다.  

  ​	

  

  