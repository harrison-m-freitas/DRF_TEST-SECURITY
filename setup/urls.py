"""
URL configuration for setup project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from school.views import StudentViewSet, CourseViewSet, RegistrationViewSet, ListRegistrationStudent, ListRegistrationCourse

router = routers.DefaultRouter()
router.register("students", StudentViewSet, basename="students")
router.register("courses", CourseViewSet, basename="courses")
router.register("registrations", RegistrationViewSet, basename="registrations")


urlpatterns = [
    path("admin", include('admin_honeypot.urls', namespace="admin_honeypot")),
    path('control/', admin.site.urls),
    path("", include(router.urls)),
    path("students/<int:pk>/registrations/", ListRegistrationStudent.as_view()),
    path("courses/<int:pk>/registrations/", ListRegistrationCourse.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
