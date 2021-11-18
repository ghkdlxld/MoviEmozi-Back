from rest_framework import serializers
from .models import Review,Review_comment,Chatboard,Chatboard_comment

class ReviewListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Review
        fields = ('title','user','updated_at')

class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class ReviewCommentListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Review_comment
        fields = ('content','user','updated_at')

class ReviewCommentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review_comment
        fields = '__all__'

class ChatboardListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chatboard
        fields=('title','user','updated_at','board_num')

class ChatboardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chatboard
        fields = '__all__'

class ChatboardCommentListSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Chatboard_comment
        fields = ('content','user','updated_at')

class ChatboardCommentSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Chatboard_comment
        fields = '__all__'


    