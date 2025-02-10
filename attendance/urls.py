from django.contrib import admin
from django.urls import include, path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mysite.urls')),
]

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
]
