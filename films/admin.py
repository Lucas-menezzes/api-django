from django.contrib import admin
from films.models import Film

class Movies(admin.ModelAdmin):
    list_display = ('id', 'name', 'gender', 'release_date', 'director','actor','box_office')
    list_link = ('id', 'name')
    search_fields = ('name', 'gender', 'director')
    list_per_page = 10

admin.site.register(Film, Movies)

