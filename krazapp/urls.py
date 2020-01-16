from django.urls import path
from .views import HomePage, PostDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView


urlpatterns = [
    path('',HomePage.as_view(), name = 'home'),
    path('post/<int:pk>',PostDetailView.as_view(), name='posts_detail'),
    path('post/new/', BlogCreateView.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name = 'post_edit'),
    path('post/delete/<int:pk>', BlogDeleteView.as_view(), name='delete_post'),

]
