from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status

from school.models import Course


class CourseTestCase(APITestCase):
    
    def setUp(self):
        
        self.list_url = reverse("courses-list")
        self.course_1 = Course.objects.create(
            course_code="CTT1",
            description="COURSE TEST 1",
            level="B"
        )
        self.course_2 = Course.objects.create(
            course_code="CTT2",
            description="COURSE TEST 2",
            level="I"
        )
        self.course_3 = Course.objects.create(
            course_code="CTT3",
            description="COURSE TEST 3",
            level="A"
        )

    def test_get_courses(self):
        """Test List Courses"""
        response = self.client.get(self.list_url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
    def test_post_courses(self):
        """Test Create Course"""
        data = {
            "course_code": "CTT4",
            "description": "COURSE TEST 4",
            "level": "A"
        }
        response = self.client.post(self.list_url, data=data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        
    def test_put_course(self):
        """Test Update Course"""
        data = {
            "course_code": "CTT1",
            "description": "COURSE TEST 1 Update",
            "level": "I"
        }
        
        response = self.client.put("/courses/1/", data=data)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        
    
    def test_delete_course(self):
        """Test Not Permission Delete Course"""
        response = self.client.delete("/courses/1/")
        self.assertEquals(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED )