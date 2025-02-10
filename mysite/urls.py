from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page view (redirects if not logged in)
    path('login/', views.login_view, name='login'),  # Login page view
    path('logout/', views.logout_view, name='logout'),  # Logout view
    path('register/', views.register_view, name='register'),  # Registration page view (if you add it)
]
