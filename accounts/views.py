from django.contrib.auth import get_user_model
from django.shortcuts import get_list_or_404, get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import serializers, status

from accounts.serializers import UserSerializer, UserListSerializer

def signup(request):
    password = request.data.get('password')
    password_confirmation = request.data.get('password_confirmation')
    if password != password_confirmation:
        return Response({'error':'비밀번호가 일치하지 않습니다'}, status=status.HTTP_400_BAD_REQUEST)
    
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(request.data.get('password'))
        user.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)

def follow(request, user_pk):
    if request.user.is_authenticated:
        person = get_object_or_404(get_user_model(), pk=user_pk)
        if request.user != person:
            if person.followers.filter(pk=request.user_pk).exists():
                person.followers.remove(request.user)
            else:
                person.followers.add(request.user)
    return Response({'error':'인증되지 않은 사용자입니다'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def user_list(request):
    person = get_user_model().objects.all()
    serializer = UserListSerializer(person, many=True)
    return Response(serializer.data)
