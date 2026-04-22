from django.shortcuts import render
from django.http import HttpResponse

def home_view(request):
    return HttpResponse("Welcome to Klaw Courses")

def detail_view(request, name):
    return HttpResponse(f"This is course: {name}")

def course_list(request):
    context = {
        'title': 'Available Courses',
        'user_name': 'Albin Siby',
        'courses': ['Python', 'Django', 'HTML', 'CSS']
    }
    return render(request, 'courses/course_list.html', context)