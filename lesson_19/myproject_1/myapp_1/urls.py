from django.urls import path
from .views import PostListView, PostCreateView,  PostUpdateView, PostDeleteView


urlpatterns = [
    path('posts/', PostListView.as_view(), name='posts_list'),
    path('posts/create/', PostCreateView.as_view(), name='posts_create'),
    path('posts/<int:pk>/update/', PostUpdateView.as_view(), name='post_update'),
    path('posts/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),

]

