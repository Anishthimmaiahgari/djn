from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),  # URL for login page
    path('dashboard/', views.dashboard, name='dashboard'),  # URL for dashboard page
]
