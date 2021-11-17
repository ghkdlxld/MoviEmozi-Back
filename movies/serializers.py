from rest_framework import serializers
from .models import Movie,Shortment

class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie,
        fields = ('title','poster_path','release_date','popularity','genres','audience','runtime',)

class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie,
        fields = '__all__'

class ShortmentListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Shortment,
        fields = '__all__'