from multiprocessing import context
from django.shortcuts import render
import requests
import random
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    return render(request, 'movies/index.html')

def recommendations(request):
    base_url = 'https://api.themoviedb.org/3'
    params = {
    'api_key': '86be6a224df194a9a21faf6e63e1b00b',
    'region': 'KR',
    'language': 'ko'
    }
    path2 = f'/movie/278/recommendations'

    recommend_response = (requests.get(base_url+path2, params= params).json()).get('results')
    random_choice = random.choice(recommend_response)
    poster_path = random_choice.get('poster_path')         
    address = ('https://image.tmdb.org/t/p/w500'+poster_path)
    overview = random_choice.get('overview')
    vote = round(random_choice.get('vote_average'),1)
    title = random_choice.get('title')
    date = random_choice.get('release_date')
    id = random_choice.get('id')
    context = {
           'address' : address,
           'overview': overview,
           'vote' : vote, 
           'title' : title,
           'date' : date,
           'id' : id,
        }

    return render(request, 'movies/recommendation.html', context)