from django.urls import path
from . import views

urlpatterns = [
    # 리뷰 목록 + 작성
    path('<int:movie_pk>/reviews/', views.reviews_list_create),
    # 단일 리뷰 detail + 수정 + 삭제
    path('<int:review_pk>/review_detail/', views.review_detail),

    # 리뷰 댓글 목록 + 작성
    path('<int:review_pk>/review_comments/', views.review_comments_list_create),
    # 리뷰 댓글 삭제 
    path('review_comments/<int:review_comment_pk>/', views.review_comments_detail),
    
    # 리뷰 좋아요
    path('<int:review_pk>/review_like/', views.review_like),

    # 게시판 글 목록 + 작성 
    path('<int:board_num>/chats/', views.chats_list_create),
    # 단일 게시판 글 detail + 수정 + 삭제
    path('<int:chatboard_pk>/chat_detail/', views.chat_detail),
    # 게시글 댓글 목록 + 작성 
    path('<int:chatboard_pk>/chat_comments/', views.chat_comments_list_create),
    # 게시글 댓글 삭제 
    path('chat_comments/<int:chat_comment_pk>/', views.chat_comments_detail),

]