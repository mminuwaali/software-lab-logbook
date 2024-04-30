from . import views
from django.urls import path

app_name = "staff"
urlpatterns = [
    path("", views.index_view, name="index-view"),
    path("<id>/record/", views.detail_view, name="detail"),
    path("<id>/student/", views.student_view, name="student"),
]  
