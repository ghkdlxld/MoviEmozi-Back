from django.contrib import admin
from .models import Review,Chatboard,Review_comment,Chatboard_comment

admin.site.register(Review)
admin.site.register(Review_comment)
admin.site.register(Chatboard)
admin.site.register(Chatboard_comment)

