from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list),  
    path('course/<str:name>/', views.detail_view),
]