from django.urls import path
from . import views

urlpatterns = [
    path('',views.movie_list),
    path('boxoffice/', views.boxoffice_list),
    path('shortment/', views.shortment_list_create),
    path('<int:movie_pk>/like/', views.movie_like),
]