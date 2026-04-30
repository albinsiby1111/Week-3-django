from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet automatically provides:

    list            -> GET /courses/
    create          -> POST /courses/
    retrieve        -> GET /courses/{id}/
    update          -> PUT /courses/{id}/
    partial_update  -> PATCH /courses/{id}/
    destroy         -> DELETE /courses/{id}/
    """

    queryset = Course.objects.all()
    serializer_class = CourseSerializer