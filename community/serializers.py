from rest_framework import serializers
from .models import Review,Review_comment,Chatboard,Chatboard_comment

class ReviewListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('id','title','user','updated_at','movie_id','created_at',)

class ReviewSerializers(serializers.ModelSerializer):
    movie = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    review_like = serializers.CharField(read_only=True)
    board_num = serializers.CharField(read_only=True)
    
    class Meta:
        model = Review
        fields = '__all__'

class ReviewCommentListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Review_comment
        fields = ('id','content','user','updated_at','created_at')

class ReviewCommentSerializers(serializers.ModelSerializer):
    review = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    
    class Meta:
        model = Review_comment
        fields = '__all__'

class ChatboardListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chatboard
        fields=('id','title','user','updated_at','board_num','created_at')

class ChatboardSerializers(serializers.ModelSerializer):
    user = serializers.CharField(read_only=True)

    class Meta:
        model = Chatboard
        fields = '__all__'
    

class ChatboardCommentListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Chatboard_comment
        fields = ('id','content','user','updated_at','created_at')

class ChatboardCommentSerializers(serializers.ModelSerializer):
    chatboard = serializers.CharField(read_only=True)
    user = serializers.CharField(read_only=True)
    
    class Meta:
        model = Chatboard_comment
        fields = '__all__'


    