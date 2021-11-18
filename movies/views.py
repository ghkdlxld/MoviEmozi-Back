from django.shortcuts import render
import requests
import json
import pprint
from .models import Movie
from django.http import JsonResponse

def movie_list(request):
    pass

def box_office_list(request):
    pass

def shortment_list_create(request):
    pass

def movie_like(request):
    pass

def movie_data_update(request):
    TMDB_api_key='325094f1219be8e028e6413f560bf212'
    nums = range(1,10000)
    for num in nums:
        try:
            video_url = f'https://api.themoviedb.org/3/movie/{num}/videos?api_key={TMDB_api_key}&language=ko-KR'
            video = requests.get(video_url).json()
            if video['results']:
                video_id = video['results'][0]['key']     # 추후 vue의 iframe api 요청보낼때의 video_id 값
                
                url = f'https://api.themoviedb.org/3/movie/{num}?api_key={TMDB_api_key}&language=ko-KR'
                data = requests.get(url).json()
                title = data['title']
                overview = data['overview']
                release_date = data['release_date']
                poster_path = data['poster_path']
                popularity = data['popularity']
                runtime = data['runtime']
                genre_list = data['genres']
                genres = []
                for genre in genre_list:
                    genres.append(genre['name'])

                Movie.objects.create(
                    title = title,
                    overview = overview,
                    release_date = release_date,
                    poster_path = poster_path,
                    popularity = popularity,
                    video_id = video_id,
                    genres = genres,
                    runtime = runtime,
                )
            else:
                pass
        except:
            pass
    return JsonResponse(data)
        

