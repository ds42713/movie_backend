from django.contrib import admin
from django.db import router
from django.urls import path , include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('movie-viewsets', views.MovieViewsets)


urlpatterns = [
    path('movie/',views.MovieGenericsView.as_view()),
    path('category/',views.CategoryAPIView.as_view()),
    path('movie/<int:id>/',views.MovieItemView.as_view()),
    path('', include(router.urls)),
]
