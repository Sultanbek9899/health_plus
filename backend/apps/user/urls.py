from django.urls import path, include
from django.contrib.auth.views import LogoutView
from .views import RegisterPage, change_password
from .views import CustomLoginView
from django.contrib.auth.views import PasswordChangeView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='index_url'), name='logout'),
    path('register/', RegisterPage.as_view(), name='register'),

    path('change-password/', change_password, name='change_password'),
]

