from django.urls import path
from .views import HomePage, PostDetailView


urlpatterns = [
    path('',HomePage.as_view(), name = 'home'),
    path('post/<int:pk>',PostDetailView.as_view(), name='posts_detail'),
]
