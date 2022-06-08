## PJT08 TIL

### Step 1 Pagination

명세서에 적혀져 있는대로 영화의 전체 목록을 모두 다 보여주기에는 몇가지 문제점이 있었다. 

첫번째로, 영화의 목록의 수가 너무 많다보니까 한번에 로드되는 시간이 걸리고 두번째로, 정리가 안된 목록의 페이지 느낌이나서 pagination 혹은 infinite scroll 두가지의 옵션 중 선택하여  idex.html을 나타낼 수 있었다. 그 중 이번에 적용한 방법은 바로 pagination이다. 

pagination을 하기 위해서는 가장 먼저 view 부분에서 page 별로 나눌 필요가 있다.

```python
# movies/views.py
@require_safe
def index(request):
    movies = Movie.objects.all()
    paginator = Paginator(movies, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'movies': page_obj,
    }
    return render(request,'movies/index.html', context)
```

위와 같이 한 페이지당 10개씩 끊어서 index.html에 전달하는 형식의 view 함수를 적용한 후,

```html
 <div class="d-flx justify-content-center pagination">
      <span class="step-links">
          {% if movies.has_previous %}
              <a href="?page=1">&laquo; first</a>
              <a href="?page={{ movies.previous_page_number }}">previous</a>
          {% endif %}
  
          <span class="current">
              Page {{ movies.number }} of {{ movies.paginator.num_pages }}.
          </span>
  
          {% if movies.has_next %}
              <a href="?page={{ movies.next_page_number }}">next</a>
              <a href="?page={{ movies.paginator.num_pages }}">last &raquo;</a>
          {% endif %}
      </span>
     

```

Django에 나와있는 코드를 참조하여 위와 같이 작용하면 pagination을 적용할 수 있다. 

### Step2. 효과 주기

마우스에 올려져 있을때나 혹은 클릭 이런 상황에서 효과를 주는 방법은 여러가지로 다양한데, 가장 먼저 CSS를 활용하거나 hover를 활용해야 한다. 하지만, 이번에 사용한 방법은 js 에서 함수를 만들어서 이러한 함수를 위의 태그에 적용하는 방법이다.

```js
function zoomIn(event) {
            event.target.style.transform = "scale(1.2)"; //1.2배 확대
            console.log(event)
            event.target.style.zIndex = 1;
            event.target.style.transition = "all 0.5s";// 속도
        }
        
function zoomOut(event) {
            event.target.style.transform = "scale(1)";
            event.target.style.zIndex = 0;
            event.target.style.transition = "all 0.5s";
        }       
    const smile = document.querySelector('#smile')
    smile.addEventListener('click', function (event) {
                        
    })   
```

위와 같이 zoomIn 과 zoomOut 함수를 js에서 만든다. 그리고 나서 줌인 줌아웃을 onmouseenter와 onmouseleave 옵션에 아래와 같이 할당하면 된다.

```html
 <i onmouseenter = "zoomIn(event)" onmouseleave="zoomOut(event)" id = "smile" class="fa-solid fa-face-grin-beam" ></i>
```



### Step3. 추천 시스템 만들기

내가 만든 추천 시스템은 사용자의 기분에 따라 추천을 달리하는 영화 시스템이다. 예를 들어 오늘 기분이 어떻고 싶냐고 하는 질문에 여러 이모티콘들이 대답칸에 나오고 이 이모티콘을 선택할 경우, 그 이모티콘 기분에 적합한 장르의 영화를 추천하는 것이다. 예를 들어 smile 이모티콘을 선택한 경우, 코미디 장르의 영화를 추천하다. 이를 좀더 간단히 구현하기 위해서 smile cry 등 여러 이모티콘에 장르 번호와 함께 함수로 넘어갈 수 있도록 구현하였다.

```html
 <a href="{% url 'movies:todetail' 35 %}">
        <i onmouseenter = "zoomIn(event)" onmouseleave="zoomOut(event)" id = "smile" class="fa-solid fa-face-grin-beam" ></i>
    </a>
    <a href="{% url 'movies:todetail' 10751 %}">
        <i onmouseenter = "zoomIn(event)" onmouseleave="zoomOut(event)" id = "cry" class="fa-solid fa-face-sad-tear"></i>

    </a>
    <a href="{% url 'movies:todetail' 10749 %}">
        
        <i onmouseenter = "zoomIn(event)" onmouseleave="zoomOut(event)" id = "love" class="fa-solid fa-face-grin-hearts"></i>    
    </a>  
    <a href="{% url 'movies:todetail' 28 %}">
        <i onmouseenter = "zoomIn(event)" onmouseleave="zoomOut(event)" id = "action" class="fa-solid fa-face-grin-squint"></i>
        
    </a>  
    <a href="{% url 'movies:todetail' 27 %}">
        <i onmouseenter = "zoomIn(event)" onmouseleave="zoomOut(event)" id = "scary" class="fa-solid fa-face-surprise"></i>     
        
   
```

이렇게 장르 번호와 함께 내가 새로 만든 함수로 넘어가면 그 장르 번호에 따른 영화들을 filter를 사용해 movies에 저장한후 새로운 html로 넘어간다. 

```python
# urls.py
app_name = 'movies'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_pk>/', views.detail, name='detail'),
    path('recommended/', views.recommended, name='recommended'),
    path('todetail/<int:genre_pk>', views.todetail, name='todetail')    
]

# movies/views.py
@require_safe
def recommended(request):
    
    movies = Movie.objects.filter(genres = 12)
    context = {
        'movies' : movies
    }     
    return render(request, 'movies/recommended.html', context)

def todetail(request, genre_pk):

    movies = Movie.objects.filter(genres = genre_pk)
    context = {
        'movies' : movies
    }
    return render(request, 'movies/todetail.html', context)
    
```

위의 함수는 recommended 라는 주소로 들어왔을 경우이고 아래의 함수는 이모티콘을 클릭했을 때, 적용되는 함수이다. 이렇게 filter로 선택된 영화들은 새로운 html에 가서 그 목록을 출력하게 된다. 

