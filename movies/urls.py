from django.urls import path
from . import views

urlpatterns = [
    path('',views.movie_list),
    path('<username>/like_users/', views.movie_user),
    path('<int:movie_pk>/shortment/', views.shortment_list_create),
    path('<int:movie_pk>/shortment_list/', views.shortment_list),
    path('shortments/<int:shortment_pk>/', views.shortment_update_delete),
    path('<int:movie_pk>/rank/', views.movie_rank),
    path('ranks/<int:user_pk>/rank_update/', views.rank_update_delete),
    path('<int:movie_pk>/like/', views.movie_like),
    path('movie_data_update/', views.movie_data_update), # api 요청보내는 url
    path('boxoffice_update/', views.boxoffice_update)
]