from django.urls import path
from . import views

urlpatterns = [
    path('',views.movie_list),
    path('shortment/', views.shortment_list_create),
    path('<int:movie_pk>/like/', views.movie_like),
    path('movie_data_update/', views.movie_data_update), # api 요청보내는 url
]