from django.contrib import admin
from django.urls import path, include
from films.views.create import MovieViewSet
from rest_framework import routers

router = routers.DefaultRouter()

router.register('movies', MovieViewSet, basename='Movies')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
