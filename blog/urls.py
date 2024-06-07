from django.urls import path
from . import views

urlpatterns = [
    path(route='home/', view=views.home, name='blog-home'),
    path(route='', view=views.home, name='blog-home'),
    path('about/', views.about, name='blog-about')
]
