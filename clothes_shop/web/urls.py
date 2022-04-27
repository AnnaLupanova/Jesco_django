from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name = 'home'),
    path('catalog', views.viewsAllCatalog, name='catalog'),
    path('<int:pk>', views.ViewDetailsProduct.as_view(), name= 'view_detail_product')
]