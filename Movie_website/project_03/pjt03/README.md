## Project03 TIL



### 1. Nav bar 코드 사용하여 원하는 Nav-bar 커스텀하기 

- Nav-bar 처음 코드를 수정하여 생각하는 Nav-bar를 만든다. 

  ```html
  <nav class="d-flex sticky-top navbar-expand-md align-items-center navbar navbar-dark  bg-dark m-0">
      <div class="container-fluid justify-content-between p-0">
        <div>
          <a href="02_home.html">
            <img src="images\logo.png" alt="로고 이미지" class="logo">
          </a>
        </div>      
  ```

- fixed-top을 줄 경우 현재의 경우와는 상관없지만, Nav-bar 아래의 글이나 그림이 Na-bar 밑으로 갈 수 있는 경우가 있기 때문에 sticky-top을 사용함. 위의 경우에는 둘 중 아무거나 사용해도 됨.

- container에 justify-content-between을 사용하여 Nav 버튼들을 끝쪽으로 보내려고 했지만 아무래도 가져온 Nav-bar 코드의 expand 기능과 햄버거 버튼의 영향으로 바뀌지를 않았다. 

  ```html
  <button class="navbar-toggler" type="button" data-bs-toggle="offcanvas" data-bs-target="#navbarOffcanvasLg" aria-controls="navbarOffcanvasLg">
          <span class="navbar-toggler-icon">
          </span>
        </button>
  
        <div class="offcanvas offcanvas-start d-flex " tabindex="-1" id="navbarOffcanvasLg" aria-labelledby="navbarOffcanvasLgLabel">
          <ul class="d-flex list-unstyled align-items-center m-0 p-0 justify-content-end" >
            <li class="nav-item">
              <!-- active 클래스! -->
              <a class="nav-link active" aria-current="page" href="02_home.html">Home</a>
                
  ```

- 이를 해결하기 위해서 페이지 검사를 한 결과 Nav-bar 버튼 뒤가 보라색으로 빈 공간임을 확인하여 리스트 클래스에 justify-content-end를 사용하여 끝쪽으로 보냈다. 

- 하지만 기존의 코드를 수정하는 작업 중 버튼들의 색이 바뀌질 않았고 결국 active와 nonactive라는 새로운 클래스를 만들어 색깔을 직접 지정해 주는 작업을 하였다. 

  ```css
  .logo {
      width: 10rem;
    }
  .active{
      color: white;
  }
  .nonactive{
      color: gray;
  }
  ```



### 2. modal 사용하기

```html
<div class="modal fade" id="productModal-1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <--중략-->
  </div>
```

- 위와 같이 로그인 화면에 쓰일 modal 코드를 Bootstap에서 가져와 body안에 쓰고 약간씩 수정하였다. modal 사용시 가장 주의할 점은 href에 수정하는 것이 아니라 아래같이id값을 맞춰서 코드를 작성해야한다. 

  ```html
  <li class="nav-item">
              <a class="nav-link nonactive" href="#" data-bs-toggle="modal" data-bs-target="#productModal-1">login</a>
            </li>
  
  <div class="modal fade" id="productModal-1" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">Login</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>             
  ```

- 그 다음으로는 클릭시 다른 페이지로 넘어가기 위해서 href에 상대경로를 넣어준다

### 3. Grid System 사용

- 화면의 넓이에 따라서 게시판과 게시판 목록의 할당되는 공간을 설정하기 위해서는 Bootstap의 Grid System을 사용해야 한다. 

```html
<div class="container">
      <div class="row"> 
        <aside class="col-lg-2 mt-2 ">
          <div class="list-group">
            <a href="#" class="list-group-item list-group-item-action" style="color: blue;">Boxoffice</a>
            <a href="#" class="list-group-item list-group-item-action" style="color: blue;">Movies</a>
            <a href="#" class="list-group-item list-group-item-action" style="color: blue;">Genres</a>
            <a href="#" class="list-group-item list-group-item-action" style="color: blue;">Actors</a>
          </div>
        </aside>
```

- Grid System을 사용하기 위해서는 최대 어디까지 적용할 것이지 범위를 클래스 container와 row안에 넣어준다. 그 다음 요소들의 클래스에 col-범위-size 형식으로 지정해준다. size는 최대 12로 그에 맞는 비율로 지정해주면 된다. 



### 4. Grid System 응용

- Grid System을 응용하여 사라짐과 나타남을 지정해주는 코드를 활용하면 화면의 넓이에 따라 변환하는 테이블, 리스트 등을 만들 수 있다. 

```html
<section class="col-lg-10 mt-2 ">
          <div class="d-none d-lg-block" >
            <table class="table">
              <thead class="table-dark">
                <tr>
                  <th scope="col">영화제목</th>
                  <th scope="col">글 제목</th>
                  <th scope="col">작성자</th>
                  <th scope="col">작성 시간</th>
                </tr>
              </thead>
                <중략>
<!-- 새로운 리스트 -->
<article class="col-12 mt-2">
          <div class="d-block d-lg-none">
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <h3>Best Movie ever</h3>
                <p>Great Movie Title</p>
                <p>1 minutes age</p>
```

- 위의 클래스에 있는 코드 처럼 특정 범위에서 없애고 싶은 경우 d-범위-none을 하고 나타나게 하고 싶을 경우 d-범위-block을 사용하면 된다. 기본의 경우 d-block이 되고 있으니 기본 값을 없는 값으로 하고 싶으면 d-none을 하면 된다. 
- 예를 들어, 첫번째 테이블은 없다가 lg이상이면 나타나는데 section 클래스가 col-lo-10이기 때문에 10자리만큼 차지한다고 보면 된다. 두번째 리스트의 경우는 기본적으로는 12만큼 자리를 차지하고 있다가 범위가 lg이상이 되면 사라진다.