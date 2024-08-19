
from .views import TeacherWeb,CourseWeb,CourseModulWeb,StudentWeb,StudentCommentWeb,QuestionsWeb
from django.urls import path,re_path,include
from rest_framework import routers



roter=routers.DefaultRouter()
roter.register(r'teacher-web/',TeacherWeb,basename='teacher-web')
roter.register(r'course-web/',CourseWeb,basename='course-web')
roter.register(r'coursemodul-web/',CourseModulWeb,basename='coursemodul-web')
roter.register(r'student-web/',StudentWeb,basename='student-web')
roter.register(r'student-comment-web/',StudentCommentWeb,basename='student-comment-web')
roter.register(r'questions-web/',QuestionsWeb,basename='questions-web')


urlpatterns=[
    path('',include(roter.urls)),
]

