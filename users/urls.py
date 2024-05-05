from django.urls import path

from users.views import UserListView, UserRegisterView, UserDetailView, UserDownloadView

app_name = 'users'

urlpatterns = [
    path('', UserListView, name='list'),
    path('register/', UserRegisterView, name='register'),
    path('<int:pk>/', UserDetailView, name='detail'),
    path('download/<int:pk>/', UserDownloadView, name='download'),
]
