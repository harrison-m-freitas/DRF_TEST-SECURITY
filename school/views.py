from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from school.models import Student, Course, Registration
from school.serielizer import (
    StudentSerializer, 
    CourseSerializer, 
    RegistrationSerializer, 
    ListRegistrationStudentSerializer,
    ListRegistrationCourseSerializer    
)


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """Show all students"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class CourseViewSet(viewsets.ModelViewSet):
    """Show all courses"""
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class RegistrationViewSet(viewsets.ModelViewSet):
    """List all registrations"""
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    
class ListRegistrationStudent(generics.ListAPIView):
    """List all studets registrations"""
    def get_queryset(self):
        queryset = Registration.objects.filter(student_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationStudentSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
class ListRegistrationCourse(generics.ListAPIView):
    """List all studets registrations"""
    def get_queryset(self):
        queryset = Registration.objects.filter(course_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListRegistrationCourseSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]