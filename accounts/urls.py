from django.urls import path
from . import views
from rest_framework_jwt.views import obtain_jwt_token
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('recom/', views.recommend),
    path('signup/', views.signup),
    path('<int:user_pk>/follow/', views.follow),
    path('userlist/', views.user_list),
    path('api-token-auth/', obtain_jwt_token),
    path('<str:name>/',views.user_detail),
    path('upload/',views.analyze_image),
    
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 