from django.shortcuts import get_list_or_404, get_object_or_404, render
from requests.models import to_native_string
from community import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import Review_comment,Review,Chatboard,Chatboard_comment
from rest_framework.decorators import api_view

@api_view(['GET'])
def reviews_list(request):
    reviews = Review.objects.all()
    serializer = serializers.ReviewListSerializers(reviews,many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET','POST'])
def reviews_list_create(request,movie_pk):
    if request.method == 'GET':
        reviews = get_list_or_404(Review,movie=movie_pk)
        serializer = serializers.ReviewListSerializers(reviews, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        if request.user.is_authenticated:
            serializer = serializers.ReviewSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, movie_id=movie_pk)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method == 'GET':
        serializer = serializers.ReviewSerializers(instance=review)
        return Response(serializer.data)
    elif request.user.is_authenticated:
        if request.method == 'PUT':
            serializer = serializers.ReviewSerializers(instance=review,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            review.delete()
            data = {
                'delete' : f'리뷰 {review_pk} 번이 삭제되었습니다'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET','POST'])
def review_comments_list_create(request,review_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Review_comment,review=review_pk)
        serializer = serializers.ReviewCommentListSerializers(comments, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = serializers.ReviewCommentSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, review_id= review_pk)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET','PUT','DELETE'])
def review_comments_detail(request,review_comment_pk):
    comment = get_object_or_404(Review_comment,pk=review_comment_pk)
    if request.method == 'GET':
        serializer = serializers.ReviewCommentSerializers(comment)
        return Response(serializer.data)
    elif request.user.is_authenticated:
        if request.method == 'PUT':
            serializer = serializers.ReviewCommentSerializers(instance=comment,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            comment.delete()
            data = {
                'delete': f'댓글{review_comment_pk}번이 삭제되었습니다.'
            }
            return Response(data,status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
        

@api_view(['POST'])
def review_like(request, review_pk):
    if request.user.is_authenticated:
        review = get_object_or_404(Review,pk=review_pk)
        if review.like_users.filter(pk=request.user.pk).exists():
            review.like_users.remove(request.user)
        else:
            review.like_users.add(request.user)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','POST'])
def chats_list_create(request):
    if request.method == 'GET':
        chats = get_list_or_404(Chatboard)
        serializer = serializers.ChatboardListSerializers(chats, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    else:
        if request.user.is_authenticated:
            serializer = serializers.ChatboardSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','PUT','DELETE'])
def chat_detail(request, chatboard_pk):
    chat = get_object_or_404(Chatboard,pk=chatboard_pk)
    if request.method == 'GET':
        serializer = serializers.ChatboardSerializers(instance=chat)
        return Response(serializer.data)
    elif request.user.is_authenticated:
        if request.method == 'PUT':
            serializer = serializers.ChatboardSerializers(instance=chat,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            chat.delete()
            data = {
                'delete' : f'게시글 {chatboard_pk} 번이 삭제되었습니다'
            }
            return Response(data, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET','POST'])
def chat_comments_list_create(request, chatboard_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Chatboard_comment,chatboard=chatboard_pk)
        serializer = serializers.ChatboardCommentListSerializers(comments, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        if request.user.is_authenticated:
            serializer = serializers.ChatboardCommentSerializers(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=request.user, chatboard_id= chatboard_pk)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET','PUT','DELETE'])
def chat_comments_detail(request,chat_comment_pk):
    comment = get_object_or_404(Chatboard_comment,pk=chat_comment_pk)
    if request.method == 'GET':
        serializer = serializers.ChatboardCommentSerializers(comment)
        return Response(serializer.data)
    elif request.user.is_authenticated:
        if request.method == 'PUT':
            serializer = serializers.ChatboardCommentSerializers(instance=comment,data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data,status=status.HTTP_200_OK)
        elif request.method == 'DELETE':
            comment.delete()
            data = {
                'delete': f'댓글{chat_comment_pk}번이 삭제되었습니다.'
            }
            return Response(data,status=status.HTTP_204_NO_CONTENT)
    else:
        return Response(status=status.HTTP_401_UNAUTHORIZED)
