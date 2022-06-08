## Project06 TIL

### 1. chocieField 사용하기
ChoiceField
기본적으로 ChoiceField 는 따로 존재하지 않습니다. 그렇기 때문에 다른 field 에 choice의 기능을 추가해줘야하는데 CharField 를 기본으로 합니다. 

```python
genre_choices = (('코미디','코미디'), ('러브코미디','러브코미디'), ('느와르','느와르'))
genre = forms.ChoiceField(choices= genre_choices)
```

NATIONAL_CHOICES 라는 2중 튜플을 만들고 이를 CharField 에 choices 옵션과 연결 해줍니다. 이럴 경우, 튜플의 앞에 값은 db에 저장되는 값, 뒤에 값은 admin 페이지나 폼에서 표시하는 값이 된다. templates 에서 값 출력 template 변수를 통해서 db에 저장된 값을 출력할 수가 있습니다.

### 2. detail 에서 update 넘어갈때 문제점 

```python
{% extends 'base.html' %}

{% block content %}
<h1>UPDATE</h1>

<form method="POST">
  {% csrf_token %}
  {{ form }}
  <button>SUBMIT</button>
</form>

<a href= "{% url 'movies:detail' movie.pk %}">Cancel</a>
{% endblock content %}
<hr>
<a href="{% url 'movies:index' %}">BACK</a>
```

위에서 보다시피 update.html에서 movies:detail 를 쓰기 때문에 movie의 정보를 넘겨줬어야했다. 

```python
def update(request, pk):
    
    movie = get_object_or_404(Movie, pk=pk)

    if request.method == 'POST':
        request.POST
        form = MovieForm(request.POST, instance=movie)
        if form.is_valid():
            movie = form.save()
            return redirect('movies:detail', movie.pk)
    else:
        
        form = MovieForm(instance = movie)
	
    context = {
        'movie' : movie,
        'form': form
    }
    return render(request, 'movies/update.html', context)
```

그래서 update 함수에 context에 원래는 form만 들어가도 되지만, form뿐만 아니라 movie를 넣어주어야 한다. 

