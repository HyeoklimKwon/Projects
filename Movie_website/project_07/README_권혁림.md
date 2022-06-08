## pjt 07 TIL

1. 제일 많이 쓰는 구문 

이번 프로젝트를 하면서 계속해서 사용했던 코드는 크게 두 가지 였다. 일단 웹 사이트 로그인 기능을 이용해서 댓글과 게시글을 작성할 수 있게 만들어야 했기 때문에 어떤 경로를 들어가든지 지속적으로 로그인 상태인지 확인하고 만약 로그인 상태가 아닐 경우, 다시 로그인 페이지로 반환하는 함수의 형태를 취해야 했다. 이를 구현할 수 있는 방법은 두가지이다. 

첫번째로, 

```python
def update(request, pk):
    if request.user.is_authenticated:
        # 이것과 같이 if문을 사용하는 방법이 있다.
        movie = get_object_or_404(Movie, pk=pk)
		(중략)
       update.html', context)
    return redirect('accounts:login')
```

두번째로,

```python
from django.views.decorators.http import require_http_methods, require_POST, require_safe
@require_POST
def comment_delete(request, movie_pk ,comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        
        comment.delete()
    return redirect('movies:detail', movie_pk)
# 데코레이터를 import 하여 하는 방법이 있다. 
```



그 다음으로는 , 댓글 작성을 제외한 나머지 게시글 작성 혹은 비밀번호 변경, 이메일 변경, 회원가입 기능들을 구현할때 처음에는 기본적인 form을 가져오고 그 다음 정보를 입력한 후에, 다시 post로 제출하여 저장하는 방식의 코드를 구현한다. 

```python
if request.method == 'POST':
    # POST 일때는 form 저장 
            form = MovieForm(request.POST)
            if form.is_valid():
                movie = form.save()
                return redirect('movies:detail', movie.pk)
        else:
            # 그외에 GET일 경우에는 기본 폼을 가져오기 ..
            # form instance <= form class
            form = MovieForm()
        # POST 쪽에서도 활용할 수 있도록
        context = {
            'form': form
        }
        return render(request, 'movies/create.html', context)
    return redirect('accounts:login')
```



2. 오류 디버깅

첫번째 오류는 cleaned data() 오류였다. 이는 form이 valid인지 확인 작업을 거쳐야지만 그 form안의 데이터를 cleaned data로 정의한다. 만약 이 과정을 작성하지 않을 경우, cleaned data 오류가 난다. 

오류 디버깅을 할때는 trace 페이지를 확인하고 어디서 부터 잘못되었는지 확인을 한다. 그 후에 해당 함수가 작성된 documents에 가서 어떤 클래스를 상속받고 안에 정의된 함수가 무엇을 확인하고 넣어야하는지 확인을 해야한다. 

