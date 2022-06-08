

## PJT08 TIL

### 1.  데이터 로딩하기 

명세서에 적힌 내용으로는 Movies 와 Actors 그리고 Movies에 따른 Reivews들로 구성하게 적혀있었다. 상식적으로 Movies에 관련 배우들이 M:N 관계 그리고 Reviews들이 1:N 관계로 Modelling을 적용하였다. 하지만, 모델을 적용한 후, 이에 주어진 데이터를 구성하는데 문제가 생겼다. 

```json
{
    "model": "movies.movie",
    "pk": 1,
    "fields": {
        "title": "Act why team bag tell over smile themselves.",
        "overview": "Once feeling according. Follow several Republican best about accept.\nAgency play what report. Know sound shoulder small.",
        "release_date": "1978-01-22T12:48:49Z",
        "poster_path": "New fish right agreement night. Create name yet smile pay west.\nEvent cause method exist detail new. Fire stand happen focus allow eye.",
        "actors": [
            6
        ]
    }
},
```

위와 같이 movies.json에 actors의 id가 적용된 형태로 기본 데이터가 주어졌기때문에 모델 구성을 할떄 actor에 ManyToManyField를 적용해야 한다. 그래서 이를 위해서 바꿨지만, 계속해서 적용이 안되는 상황이 발생하였다. 

이를 해결하기 위해, 또 db를 초기화(삭제)를 함과 동시에 migration 파일에 있는 기록들 (번호가 있는 python 파일들 )을 지우고 아래와 같이 모델을 변경하여 해결하였다.

```python
from django.db import models

class Actor(models.Model):
    name = models.CharField(max_length= 100)
    
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length= 100)
    overview = models.TextField()
    release_date = models.DateTimeField()
    poster_path = models.TextField()
    actors = models.ManyToManyField(Actor, related_name= 'movies')


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete= models.CASCADE)
    title = models.CharField(max_length= 100)
    content = models.TextField()
```

### 2. Review 조회할때 movie정보도 같이 조회하기 

보통 serializer을 일반적으로 구성할 때, review 정보를 조회하면, movie 정보중 movie_id 값만 출력되게 된다. 이를 해결하기 위해서는 해당 영화정보를 출력하기 위해 새로운 MovieTitleSerializer를 만든다.  그리고 movie에 그 시리얼라이저를 넣어주면 끝이다  하나의 시리얼라이저안에 그 모델이 지닌 필드가 a라고 한다면 여기서는 User가 movie 라는 필드를 가지고 있는 것이기에 (MtoM으로 미리 연결하였기 때문에) 

movie = serializer(many=True) 만 해줘도movie 안에 영화 정보만 나오게 된다.

```python
class MovieTitleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Movie
        fields = ('title',)

class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieTitleSerializer()

    class Meta:
        model = Review        
        fields = '__all__'
        
```

### 3. 생성 및 갱신할때 movie 정보도 같이 출력하기

```python
@api_view(['GET', 'DELETE', 'PUT'])
def review_detail(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        # movie_pk = serializer.data.get('movie')
        # movie = get_object_or_404(Movie, pk = movie_pk)
        # serializer.data.movie = movie.title                  
        return Response(serializer.data) 

    elif request.method == 'DELETE':
        review.delete()
        data = {
            'delete': f'데이터 {review_pk}번 리뷰가 삭제되었습니다.',
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT':
        serializer = ReviewUpdateSerializer(review, request.data)
        # serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            review_pk = serializer.data['id']
            review = get_object_or_404(Review, pk=review_pk)
            serializer = ReviewSerializer(review)
            return Response(serializer.data)

# Review 생성
@api_view(['POST'])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewCreateSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie = movie)
        review_pk = serializer.data['id']
        review = get_object_or_404(Review, pk=review_pk)
        serializer = ReviewSerializer(review)        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
```

위의 것을 응용하여 , 생성 될때, reivew_pk를 가져와서 이를 다시 Reviewserializer에 넣어서 그 리뷰의 디테일 페이지로 리다이렉트하는 코드를 구성하였다. 