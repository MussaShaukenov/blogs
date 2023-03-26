from django.urls import path
from .views import (
    CardListView,
    CardCreateView,
    CardUpdateView,
    CardDeleteView,
    CardDetailView,
    CategoryListView,
    CategoryDetailView,
    CategoryCreateView,
    CategoryUpdateView,
    CategoryDeleteView,
    SearchView,
)

urlpatterns = [
    path('', CardListView.as_view(), name='card_list'),
    path('card/new/', CardCreateView.as_view(), name='card_create'),
    path('card/<int:pk>/detail', CardDetailView.as_view(), name='card_detail'),
    path('card/<int:pk>/edit/', CardUpdateView.as_view(), name='card_update'),
    path('card/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
    path('category/', CategoryListView.as_view(), name='category_list'),
    path('category/new/', CategoryCreateView.as_view(), name='category_create'),
    path('category/<int:pk>/detail', CategoryDetailView.as_view(), name='category_detail'),
    path('category/<int:pk>/edit/', CategoryUpdateView.as_view(), name='category_update'),
    path('category/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),
    path('search', SearchView.as_view(), name='search')
]
