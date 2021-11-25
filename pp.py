from datetime import datetime
import requests
import pprint
# from movies.models import Movie

KOFIC_API = '4264dfeb35de00f9b3425f81600289c2'
TMDB_API = '325094f1219be8e028e6413f560bf212'

now = datetime.now()    
today = int(now.strftime("%Y%m%d"))-7

boxoffice_url= f"http://kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchWeeklyBoxOfficeList.json?key={KOFIC_API}&targetDt={today}&weekGb=0"
boxoffice_movies = requests.get(boxoffice_url).json()
movie_list = boxoffice_movies['boxOfficeResult']['weeklyBoxOfficeList']

box_movie_title = []
for movie in movie_list:
    box_movie_title.append(movie['movieNm'])

print(box_movie_title)
box_movie_info = []
for title in box_movie_title:
    
    tmdb_url = f'https://api.themoviedb.org/3/search/movie?api_key={TMDB_API}&language=ko-KR&page=1&include_adult=false&query={title}'
    data = requests.get(tmdb_url).json()['results'][0]
    pprint.pprint(data)
    # genre_list = data['genres']
    # genres = []
    # for genre in genre_list:
    #     genres.append(genre['name'])
    # movie_id = data['results'][0]['id']
    # video_url = f'https://api.themoviedb.org/3/movie/{movie_id}/videos?api_key={TMDB_API}&language=ko-KR'
    # video = requests.get(video_url).json()
    # if video['results']:
    #     video_id = video['results'][0]['key']
    # else:
    #     video_id = ''
    
    # Movie.objects.create(
    #     title = data['title'],
    #     overview = data['overview'],
    #     release_date = data['release_date'],
    #     poster_path = data['poster_path'],
    #     popularity = data['popularity'],
    #     runtime = data['runtime'],
    #     video_id = video_id,
    #     genres = genres,
    #     backdrop_path = data['backdrop_path'],
    #     status = data['status'],
    #     vote_average = data['vote_average'],
    #     vote_count = data['vote_count'],
    #     adult = data['adult']
    #     )