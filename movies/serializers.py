import re
from rest_framework import serializers
from .models import Movie,Shortment

class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('title','poster_path','release_date','popularity','genres','runtime',)

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class ShortmentListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Shortment
        fields = '__all__'

class ShortmentSerializers(serializers.ModelSerializer):
    movie_id = serializers.CharField(read_only=True)

    class Meta:
        model = Shortment
        fields = ('id','content','movie_id',)