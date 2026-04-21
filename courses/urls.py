from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    path('course/<str:name>/', views.course_detail, name='course_detail'),
]
