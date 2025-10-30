from .views import index
from django.urls import path
from . import views

urlpatterns = [
    path("", index,  name="index"),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/<int:product_id>/rate/', views.product_rate, name='product_rate'),
]