from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('product_list', views.list_product, name='product_list'),
    path('product_details/<int:pk>', views.detail_product, name='product_details')
    ]