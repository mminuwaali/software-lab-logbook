from . import views
from django.urls import path

app_name = 'account'
urlpatterns = [
    path('login/', views.login_view, name='login-view'),
    path('logout/', views.logout_view, name='logout-view'),
    path('register/', views.register_view, name='register-view'),
]