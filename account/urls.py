from django.urls import path
from account import views

urlpatterns = [
    path('sign-in/', views.signIn),
    path('sign-up/', views.signUp),
    path('sign-out/', views.signOut),
    path('profile/', views.profile),
    path('profile/password/', views.profilePassword),
    path('profile/avatar/', views.profileAvatar),
]
