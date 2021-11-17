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

class ReviewCommnetSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Review_comment
        fields = ('content','user','updated_at')

class ChatboardListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chatboard
        fields=('title','user','updated_at')

class ChatboardSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chatboard
        fields = '__all__'

class ChatboardCommnetSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Chatboard_comment
        fields = ('content','user','updated_at')


    