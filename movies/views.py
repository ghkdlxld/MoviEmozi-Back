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
    nums = range(1,100)
    for num in nums:
        try:
            url = f'https://api.themoviedb.org/3/movie/{num}?api_key={TMDB_api_key}&language=ko-KR'
            data = requests.get(url).json()
            video_url = f'https://api.themoviedb.org/3/movie/{num}/videos?api_key={TMDB_api_key}&language=ko-KR'
            title = data['title']
            overview = data['overiew']
            release_date = data['release_date']
            poster_path = data['poster_path']
            popularity = data['popularity']
            video = requests.get(video_url).json()
            pprint.pprint(video)
            if video:
                video_id = video[0]['key']     # 추후 vue의 iframe api 요청보낼때의 video_id 값
            # genre_list = data['genres']
            # genres = []
            # for genre in genre_list:
            #     genres.append(genre['name'])
                pprint.pprint(video_id)
                genres = data['genres'][0]['name']
                runtime = data['runtime']
                Movie.objects.create(
                    title = title,
                    overview = overview,
                    release_date = release_date,
                    poster_path = poster_path,
                    popularity = popularity,
                    video_id = video_id,
                    genres = genres,
                    runtime = runtime
                )
                return JsonResponse({'title':title})
        except:
            pass
    return JsonResponse(data)
        

