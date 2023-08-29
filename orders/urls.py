from django.urls import path
from orders import views

urlpatterns = [
    path('basket/', views.basket),
    path('orders', views.orders),
    path('order/<int:id>', views.order),
    path('payment/<int:id>', views.payment),
]
