from django.conf import settings
from django.http.response import JsonResponse
from django.shortcuts import get_list_or_404, get_object_or_404, render
from requests.models import to_native_string
from community import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import Review_comment,Review,Chatboard,Chatboard_comment
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny

@api_view(['GET'])
@permission_classes([AllowAny])
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
        serializer = serializers.ReviewSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie_id=movie_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def review_detail(request,review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method == 'GET':
        serializer = serializers.ReviewSerializers(instance=review)
        return Response(serializer.data)
    elif request.method == 'PUT':
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

@api_view(['GET','POST'])
def review_comments_list_create(request,review_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Review_comment,review=review_pk)
        serializer = serializers.ReviewCommentListSerializers(comments, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.ReviewCommentSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, review_id= review_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def review_comments_detail(request,review_comment_pk):
    comment = get_object_or_404(Review_comment,pk=review_comment_pk)
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
    serializer = serializers.ReviewCommentSerializers(comment)
    return Response(serializer.data)

@api_view(['POST','GET'])
def review_like(request, review_pk):
    review = get_object_or_404(Review,pk=review_pk)
    if request.method=='GET':
        if review.review_like.filter(pk=request.user.pk).exists():
            like = True
        else:
            like = False
        context = {
            'count' : review.review_like.count(),
            'like' : like
        }
        return Response(context, status=status.HTTP_200_OK)

    elif request.method=='POST':
        if review.review_like.filter(pk=request.user.pk).exists():
            review.review_like.remove(request.user)
            liked = False
        else:
            review.review_like.add(request.user)
            liked = True

        context={
            'liked': liked,
            'count':review.review_like.count(),
        }
        return Response(context, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([AllowAny])
def chats_list(request):
    chats = get_list_or_404(Chatboard)
    serializer = serializers.ChatboardListSerializers(chats, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)


@api_view(['POST'])
def chats_list_create(request):
    serializer = serializers.ChatboardSerializers(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def chat_detail(request, chatboard_pk):
    chat = get_object_or_404(Chatboard,pk=chatboard_pk)
    if request.method == 'GET':
        serializer = serializers.ChatboardSerializers(instance=chat)
        return Response(serializer.data)
    elif request.method == 'PUT':
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


@api_view(['GET','POST'])
def chat_comments_list_create(request, chatboard_pk):
    if request.method == 'GET':
        comments = get_list_or_404(Chatboard_comment,chatboard=chatboard_pk)
        serializer = serializers.ChatboardCommentListSerializers(comments, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = serializers.ChatboardCommentSerializers(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, chatboard_id= chatboard_pk)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET','PUT','DELETE'])
def chat_comments_detail(request,chat_comment_pk):
    comment = get_object_or_404(Chatboard_comment,pk=chat_comment_pk)
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
    serializer = serializers.ChatboardCommentSerializers(comment)
    return Response(serializer.data)

# 해당 유저가 쓴 댓글 조회

@api_view(['GET'])
def review_comments_list(request,user_pk):
    comments = Review_comment.objects.filter(user_id=user_pk)
    serializer = serializers.ReviewCommentSerializers(comments, many=True)
    
    return Response(serializer.data,status=status.HTTP_200_OK)

@api_view(['GET'])
def chat_comments_list(request, user_pk):
    comments = Chatboard_comment.objects.filter(user_id=user_pk)
    serializer = serializers.ChatboardCommentSerializers(comments, many=True)
    return Response(serializer.data,status=status.HTTP_200_OK)