from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from . import views


urlpatterns = [
    #path('', views.home, name='blog-home'),
    path('', PostListView.as_view(), name='blog-home'),
    path('blog/new', PostCreateView.as_view(), name='blog-create'),
    path('blog/<int:pk>/', PostDetailView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/update', PostUpdateView.as_view(), name='blog-update'),
    path('blog/<int:pk>/delete', PostDeleteView.as_view(), name='blog-delete'),
    path('about/', views.about, name='blog-about'),
]