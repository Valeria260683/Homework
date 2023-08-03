from django.urls import path
from .views import TrainDetailView, TrainListView

urlpatterns = [
    path('trains/', TrainListView.as_view(), name='train-list'),
    path('trains/<int:pk>/', TrainDetailView.as_view(), name='train-detail'),
]