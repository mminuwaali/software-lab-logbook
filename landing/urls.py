from . import views
from django.urls import path

app_name = 'landing'
urlpatterns = [
    path('', views.index_view, name='index-view'),
    path('about-us/', views.about_view, name='about-view'),
]