## This rep is for my own projects

- Movie website: 영화 추천 + 유튜브에서 영화를 검색해서 볼 수 있게 만든 사이트

- StockRecommend: 사람들의 성격 유형에 기반하여 주식들의 포트폴리오 추천 (한국 우량주)

- 강화게임: 온라인 게임에서 사용되는 확률 기반 시스템을 재미로 구현

- 잔디가 안심어지는 현상발견 ! 

  - 이럴때는 git bash를 켜고 git config --list를 통해 github에 등록된 user.name과 user.email를 확인하고 다를 경우 git config --global user.email or user.name "유저 이메일" or '유저 이름'으로 설정해주도록 하자 
  
  - 만약에 하나의 프로젝트만 바꾸고 싶다면 git conifg user.email "내 이메일" 하면 된다.
  
  - 이미 커밋한것을 살리고 싶을 경우 rebase를 통해 살릴 수 있다. 
  
  - ```git
    git log --pretty=format:"%h = %an , %ar : %s" --graph
    # 로그들 중에서 잔디가 심어지지 않은 커밋 내역의 해쉬코드를 기억한 다음
    git rebase -i -p 해쉬코드
    #입력한다
    ```
  
    
  
