from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    path('', views.SalesList.as_view(), name='sales')
        
]

