from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup),
    path('<int:user_pk>/follow/', views.follow),
    
]