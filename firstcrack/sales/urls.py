from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.SalesList.as_view(), name='sales'),
    path('<int:pk>/', views.SaleDetail.as_view(), name='sale-detail'),
    path('products/', views.ProductList.as_view(), name="products")
    
        
]

