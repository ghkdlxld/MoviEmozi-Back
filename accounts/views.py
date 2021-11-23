from django.contrib.auth import get_user_model
from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from rest_framework.decorators import api_view, permission_classes, renderer_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import serializers, status
from .models import User,HairImage
from django.views.decorators.http import require_POST
from rest_framework.renderers import JSONRenderer
from accounts.serializers import UserSerializer, UserListSerializer
import os
import sys
import requests


@api_view(['POST'])
@permission_classes([AllowAny])
def signup(request):
    name = request.data.get('username')
    users = User.objects.all()
    if name in users:
        return Response({'error':'이미 존재하는 이름 입니다.'},status=status.HTTP_409_CONFLICT)
    else:
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            user.set_password(request.data.get('password'))
            user.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)

@api_view(['POST'])
def follow(request, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    if request.user != person:
        if person.followers.filter(pk=request.user.pk).exists():
            person.followers.remove(request.user)
            followed = False
        else:
            person.followers.add(request.user)
            followed = True
        context={
            'followed' : followed,
            'followers' : [person.followers.all().values()],
            'followings' : [person.followings.all().values()],
        }
        return Response(context,status=status.HTTP_200_OK)
    return Response({'error':'자기 자신은 팔로우할 수 없습니다.'},status=status.HTTP_406_NOT_ACCEPTABLE)
    

@api_view(['GET'])
@permission_classes([AllowAny])
def user_list(request):
    person = get_user_model().objects.all()
    serializer = UserListSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def user_detail(request,name):
    person = User.objects.filter(username=name)
    serializer = UserListSerializer(person, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@renderer_classes([JSONRenderer,])
def analyze_image(request):
    src = request.FILES['files']
    uploaded_image = HairImage.objects.create(upload_image=src, upload_user=request.user)
    return Response(status=status.HTTP_201_CREATED)

# @api_view(['POST'])
# @permission_classes([AllowAny])
@require_POST
def recommend(request):
    Client_ID = 'oTXX6kMwz__NOqLgy4dH'
    Client_Secret = 'L5ot3Ah5zY'
    api_url = 'https://openapi.naver.com/v1/vision/face'
    files = {'image': open('123.jpg', 'rb')}
    headers = {'X-Naver-Client-Id': Client_ID, 'X-Naver-Client-Secret': Client_Secret }
    response = requests.post(api_url,  files=files, headers=headers)
    print(response)
    rescode = response.status_code
    if(rescode==200):
        print (response.text)
    else:
        print("Error Code:" + rescode)