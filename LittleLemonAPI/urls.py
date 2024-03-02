# ./LittleLemonAPI/urls.py

from django.urls import path
from .views import CategoryListCreateView, MenuItemListCreateView, MenuItemRetrieveUpdateDestroyView

urlpatterns = [
    path('categories/', CategoryListCreateView.as_view(), name='category-list'),
    path('menu-items/', MenuItemListCreateView.as_view(), name='menuitem-list'),
    path('menu-items/<int:pk>/', MenuItemRetrieveUpdateDestroyView.as_view(), name='menuitem-detail'),
]
