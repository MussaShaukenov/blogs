from django.urls import path
from . import views

urlpatterns = [
    path('', views.CardListView.as_view(), name='card_list'),
    path('create/', views.CardCreateView.as_view(), name='card_create'),
    path('<int:pk>/update/', views.CardUpdateView.as_view(), name='card_update'),
    path('<int:pk>/delete/', views.CardDeleteView.as_view(), name='card_delete'),
]
