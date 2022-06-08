import json


def dec_movies(movies):
    movie_list = []
    movie_revenue_list = []
    movie_revenue = 0
    movie_date_list = []
    dec_movie_list = []
    for movie in movies:
        movie_title = movie['title']
        movie_id = movie['id']
        movie_detail_json = open(f'data/movies/{movie_id}.json',encoding='UTF8')
        movie_detail = json.load(movie_detail_json)
        movie_revenue = movie_detail['revenue']
        movie_dict = {'title' : movie_title , 'revenue' : movie_revenue}
        movie_revenue_list.append(movie_revenue)
        movie_list.append(movie_dict)

        movie_date = movie_detail["release_date"]
        movie_month = int(movie_date[5:7])
        if movie_month == 12 :
            dec_movie_list.append(movie_title)




    for revenues in movie_list:
        reven = revenues['revenue']
        if reven == max(movie_revenue_list):
            pop_movie_title = revenues['title']
    return dec_movie_list  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))