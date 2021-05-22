from django.urls import path
from .views import index, admin_users_read

app_name = 'adminapp'

urlpatterns = [
    path('', index, name='index'),
    path('admin-users-read/', admin_users_read, name='admin_users_read'),
]