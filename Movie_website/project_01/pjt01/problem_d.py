import json


def max_revenue(movies):
    movie_list = []
    movie_revenue_list = []
    movie_revenue = 0
    for movie in movies:
        movie_title = movie['title']
        movie_id = movie['id']
        movie_detail_json = open(f'data/movies/{movie_id}.json',encoding='UTF8')
        movie_detail = json.load(movie_detail_json)
        movie_revenue = movie_detail['revenue']
        movie_dict = {'title' : movie_title , 'revenue' : movie_revenue}
        movie_revenue_list.append(movie_revenue)
        movie_list.append(movie_dict)
    for revenues in movie_list:
        reven = revenues['revenue']
        if reven == max(movie_revenue_list):
            pop_movie_title = revenues['title']
    return pop_movie_title

    
        
 
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))