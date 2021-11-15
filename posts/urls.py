from django.urls import path,include
from .views import PostsListCreateView, PostsDetailsView, CommentsListCreateView, CommentsDetailsView

urlpatterns = [
    path('posts/', PostsListCreateView.as_view(), name='PostsListCreateView'),
    path('posts/<int:pk>/', PostsDetailsView.as_view(), name='PostsDetailsView'),
    path('comments/', CommentsListCreateView.as_view(), name='CommentsListCreateView'),
    path('comments/<int:pk>/', CommentsDetailsView.as_view(), name='CommentsDetailsView'),
]