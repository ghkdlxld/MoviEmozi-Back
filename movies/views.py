from django.shortcuts import get_object_or_404, render , get_list_or_404
import requests
import json
import pprint

from rest_framework.permissions import AllowAny

from movies import serializers
from .models import Movie, Shortment,Rank
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework import status


@api_view(['GET'])
@permission_classes([AllowAny])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = serializers.MovieListSerializers(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([AllowAny])
def shortment_list(request,movie_pk):
    shortments = Shortment.objects.all().filter(movie=movie_pk)
    serializer = serializers.ShortmentListSerializers(shortments, many=True)
    if shortments:
        return Response(serializer.data,status=status.HTTP_200_OK)
    return Response({}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
def shortment_list_create(request,movie_pk):
    if request.user.is_authenticated:
        serializer = serializers.ShortmentSerializers(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie_id = movie_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)



@api_view(['PUT','DELETE'])
def shortment_update_delete(request, shortment_pk):
    shortment = get_object_or_404(Shortment, pk=shortment_pk)
    if request.method == 'PUT':
        serializer = serializers.ShortmentSerializers(instance=shortment,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        shortment.delete()
        data = {
            'delete' : f'한줄평 {shortment_pk} 번이 삭제되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def movie_rank(request, movie_pk):
    if request.method == 'GET':
        rank = Rank.objects.all().filter(movie=movie_pk)
        if rank:
            serializer = serializers.RankListSerializers(rank, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response([], status=status.HTTP_204_NO_CONTENT)
    else:
        serializer = serializers.RankListSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)



@api_view(['PUT','DELETE'])
def rank_update_delete(request, user_pk):
    rank = get_object_or_404(Rank, user=user_pk)
    if request.method == 'PUT':
        serializer = serializers.RankListSerializers(instance=rank, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'DELETE':
        rank.delete()
        data = {
            'delete' : f'{user_pk}님의 평점이 삭제되었습니다'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)






@api_view(['GET', 'POST'])
def movie_like(request, movie_pk):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        user = request.user
        if request.method == 'GET':
            user_like_movie = user.like_movies
            serializer = serializers.MovieListSerializers(user_like_movie, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            if movie.like_users.filter(pk=user.pk).exists():
                movie.like_users.remove(user)
                liked = False
            else:
                movie.like_users.add(user)
                liked = True
            context = {
                'liked' : liked,
                'like_count' :movie.like_users.count()
            }
            return Response(context, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)



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
                backdrop_path = data['backdrop_path']
                status = data['status']
                vote_average = data['vote_average']
                vote_count = data['vote_count']
                adult = data['adult']
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
                    backdrop_path = backdrop_path,
                    status = status,
                    vote_average = vote_average,
                    vote_count = vote_count,
                    adult = adult,
                )
            else:
                pass
        except:
            pass
    return JsonResponse(data)
        

