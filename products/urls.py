from django.urls import path
from products import views

urlpatterns = [
    path('banners', views.banners),
    path('categories/', views.categories),
    path('catalog', views.catalog),
    path('products/popular/', views.productsPopular),
    path('products/limited/', views.productsLimited),
    path('sales', views.sales),
    path('tags/', views.tags),
    path('product/<int:id>/', views.product),
    path('product/<int:id>/reviews', views.productReviews),
]
