"""urls for myapp."""

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from myapp.views import *

router = SimpleRouter()


# router.register(r'student', StudentViews, basename='student')
router.register(r'student-profile', StudentProfileViews, basename='student-profile')
router.register(r'teacher', TeacherViews, basename='teacher')
router.register(r'subjects', SubjectViews, basename='subjects')

urlpatterns = [
    path('', include(router.urls)),
    path('add-student/', StudentClass.add_student),
    path('list-students/', StudentClass.list_students),
    path('update-student/<int:id>', StudentClass.update_student),
]