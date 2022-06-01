from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('catalog/men', views.ViewMenProducts.as_view(), name='catalog_men'),
    path('catalog/womens', views.ViewWomensProducts.as_view(), name='catalog_womens'),
    path('catalog/kids', views.ViewKidsProducts.as_view(), name='catalog_kids'),
    path('catalog', views.CatalogView.as_view(), name='catalog'),
    path('catalog/accessories', views.ViewAccessoriesProducts.as_view(), name='catalog_accessories'),
    path('catalog/shoes', views.ViewShoesProducts.as_view(), name='catalog_shoes'),
    path("catalog/filter/", views.ViewFilterProducts.as_view(), name='filter'),
    path('<int:pk>', views.ViewDetailsProduct.as_view(), name= 'view_detail_product')
]