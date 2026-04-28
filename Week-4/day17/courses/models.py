from django.db import models

# Custom Manager
class ActiveCourseManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)


# Course Model
class Course(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    is_active = models.BooleanField(default=True)

    objects = models.Manager()
    active_objects = ActiveCourseManager()

    def __str__(self):
        return self.title


# Many-to-One
class Lesson(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='lessons'
    )
    title = models.CharField(max_length=100)
    content = models.TextField()

    def __str__(self):
        return self.title


# Many-to-Many
class Student(models.Model):
    name = models.CharField(max_length=100)
    courses = models.ManyToManyField(Course)

    def __str__(self):
        return self.name


# One-to-One
class CourseDetail(models.Model):
    course = models.OneToOneField(
        Course,
        on_delete=models.CASCADE
    )
    syllabus = models.TextField()

    def __str__(self):
        return f"Details of {self.course.title}"