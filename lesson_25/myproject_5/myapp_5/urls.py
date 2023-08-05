from django.urls import path
from .views import PublisherViewSet, AuthorViewSet

urlpatterns = [
 path('publishers/', PublisherViewSet.as_view({'get': 'list', 'post': 'create'}), name='publisher-list'),
 path('authors/', AuthorViewSet.as_view({'get': 'list', 'post': 'create'}), name='author-list'),
 path('publishers/<int:publisher_id>/authors/', AuthorViewSet.as_view({'get': 'list_by_publisher'}), name='author-list-by-publisher'),
   ]