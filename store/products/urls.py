from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.catalog, name='products'),
    path('products/category/<int:category_id>/', views.catalog, name='products_category'),
    path('products/page/<int:page_number>/', views.catalog, name='paginator')
]