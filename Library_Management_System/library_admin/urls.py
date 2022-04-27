from django.contrib import admin
from django.urls import path
from . import views

app_name = 'library_admin'

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('index', views.IntexView.as_view(), name='index'),
    path('admin-register', views.AdminRegisterView.as_view(), name='admin-register'),
    path('admin-login', views.AdminLoginView.as_view(), name='admin-login'),
    path('admin-logout', views.AdminLogoutView.as_view(), name='admin-logout'),
    path('admin-dashboard', views.AdminDashboardView.as_view(), name='admin-dashboard'),
    path('add-book', views.AddBookView.as_view(), name='add-book'),
    path('edit-book/<int:pk>', views.EditBookView.as_view(), name='edit-book'),
    path('detail-book/<int:pk>', views.BookDetailView.as_view(), name='detail-book'),
    path('delete-book/<int:pk>', views.DeleteBookView.as_view(), name='delete-book'),
]