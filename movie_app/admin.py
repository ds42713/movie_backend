from movie_app.models import Movie
from django.contrib import admin
from .models import *

class MovieTabularInline(admin.TabularInline):
    model = MovieComment
    extra = 0

class Movie_Admin(admin.ModelAdmin):
    list_display = ['name','published']
    list_filter = ['published']
    search_fields = ['name','actor','director','film_company']
    prepopulated_fields = {'slug': ['name']}
    fieldsets = (
        (None , {'fields':['name','slug','description','published']}),
        ('Category',{'fields':['category','actor','director','film_company']})
    )
    inlines = [ MovieTabularInline ]


admin.site.register(Category)
admin.site.register(Film_company)
admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie,Movie_Admin)