from django.contrib import admin

from walken.models import Movie, File, User, Rating

admin.site.register(Movie)
admin.site.register(File)
admin.site.register(User)
admin.site.register(Rating)