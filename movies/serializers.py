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
    
    # class MovieSerializers(serializers.ModelSerializer):
    #     class Meta:
    #         model = Movie
    #         fields= ('pk','title',)

    user = serializers.CharField(read_only=True)
    movie = MovieSerializers(many=True, read_only=True)

    # movie_pk = serializers.IntegerField(write_only=True)

    def create(self, validated_data):
        movie_pk = validated_data.pop('movie_pk')
        ment = Shortment.objects.create(**validated_data)
        ment.movie.add(movie_pk)
        return ment


    class Meta:
        model = Shortment
        fields = ('id','content','user','movie','movie_pk')