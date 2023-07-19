from django.urls import path
from . import views

urlpatterns = [
    path('all_posts/', views.all_posts, name='all_posts'),
]
