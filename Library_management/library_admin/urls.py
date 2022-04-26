from django.contrib import admin
from django.urls import path
from . import views

app_name = 'library_admin'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index', views.IntexView.as_view(), name='index'),
    path('admin-register', views.AdminRegisterView.as_view(), name='admin-register'),
    path('admin-login', views.AdminLoginView.as_view(), name='admin-login'),
]
