from django.contrib import admin
from .models import Course, Lesson, Student, CourseDetail

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'is_active')


admin.site.register(Lesson)
admin.site.register(Student)
admin.site.register(CourseDetail)