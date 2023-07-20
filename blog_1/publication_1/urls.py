from django .urls import path, include
from .views import hello, page_view, PageListView


urlpatterns = [
    path('hello/', hello, name="hello"),
    path("all-pages-func/", page_view, name="all-pages-func"),
    path("all-pages-class/", PageListView.as_view(), name="all-pages-class")
]