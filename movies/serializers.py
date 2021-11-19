from rest_framework import serializers
from .models import Movie,Shortment

class MovieListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'


class ShortmentListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Shortment
        fields = '__all__'

class ShortmentSerializers(serializers.ModelSerializer):
    movie= serializers.CharField(read_only=True)

    class Meta:
        model = Shortment
        fields = ('id','content','movie')