from django.urls import path
from . import views

urlpatterns = [
    # 리뷰 목록 + 작성
    path('reviews/', views.reviews),
    # 단일 리뷰 detail
    path('<int:review_pk>/review_detail/', views.review_detail),

    # 리뷰 댓글 목록 + 작성
    path('<int:review_pk>/review_comments/', views.review_comments),
    # 리뷰 좋아요
    path('<int:review_pk>/review_like/', views.review_like),

    # 게시판 글 목록 + 작성
    path('<int:board_num>/chats/', views.chats),
    # 단일 게시판 글 detail
    path('<int:chatboard_pk>/chat_detail/', views.chat_detail),
    # 게시글 댓글 목록 + 작성 
    path('<int:chatboard_pk>/chat_comments/', views.chat_comments),


]