from django.urls import path
from .views import NewsListCreateView, NewsDetailView, CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path("news/", NewsListCreateView.as_view(), name="news-list"),
    path("news/<int:pk>/", NewsDetailView.as_view(), name="news-detail"),
    path("categories/", CategoryListCreateView.as_view(), name="category-list"),
    path("categories/<int:pk>/", CategoryDetailView.as_view(), name="category-detail"),
]
