from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from school.models import Student, Course, Registration
from school.serielizer import (
    StudentSerializer, 
    CourseSerializer, 
    RegistrationSerializer, 
    ListRegistrationStudentSerializer,
    ListRegistrationCourseSerializer,
    StudentSerializerV2
)


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """Show all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    
    def get_serializer_class(self):
        if self.request.version == "v2":
            return StudentSerializerV2
        else: 
            return StudentSerializer
    
class CourseViewSet(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    http_method_names = ['get', "post", "put", 'path',]
    serializer_class = CourseSerializer
    
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            id = str(serializer.data["id"])
            response["Location"] = request.build_absolute_uri() + id
            return response
    
    
class RegistrationViewSet(viewsets.ModelViewSet):
    """List all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    http_method_names = ['get', "post", "put", 'path', 'options']
    
    @method_decorator(cache_page(60 * 1))
    def dispatch(self, *args, **kwargs):
        return super(RegistrationViewSet, self).dispatch(*args, **kwargs)

    
    
class ListRegistrationStudent(generics.ListAPIView):
    """List all studets registrations"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentSerializer

    
class ListRegistrationCourse(generics.ListAPIView):
    """List all studets registrations"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationCourseSerializer
    