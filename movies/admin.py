from django.contrib import admin
from .models import Movie, Rank, Shortment

admin.site.register(Movie)
admin.site.register(Shortment)
admin.site.register(Rank)