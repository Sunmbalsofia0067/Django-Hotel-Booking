from django.urls import path
from . import views


urlpatterns = [
    path('register-user', views.register_user, name='register-user'),
    path('login-user', views.login_user, name='login-user'),
    path('logout', views.logoutUser, name='logout'),
    path('update-user', views.update_user, name='update-user'),
    path('update-billing', views.update_billing, name='update-billing')
]