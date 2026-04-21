from django.http import HttpResponse

def home(request):
    return HttpResponse("Welcome to Klaw Courses")

def course_detail(request, name):
    return HttpResponse(f"This is course: {name}")
