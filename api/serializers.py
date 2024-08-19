from rest_framework import serializers
from .models import Teacher,Course,CourseModul,Student,Questions,StudentComment

class TeacherSerializersWeb(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=('id','first_name','last_name','phone_number','image','status','slug')


class CourseSerializersWeb(serializers.ModelSerializer):
    teachers=TeacherSerializersWeb()
    class Meta:
        model=Course
        fields=('id','course_name','price','image','listing','teachers','slug')


class CourseModulSerializersWeb(serializers.ModelSerializer):
    course=CourseSerializersWeb
    class Meta:
        model=CourseModul
        fields=('id','course_module_name','description','image','create_at','listing','course','slug')


class StudentSerializersWeb(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields=('id','first_name','last_name','image','slug')


class StudentCommentSerializerWeb(serializers.ModelSerializer):
    student=StudentSerializersWeb()
    course_model=CourseModulSerializersWeb()

    class Meta:
        model=StudentComment
        fields=('id','comment','student','course_model','slug','listing')

class QuestionsSerializersWeb(serializers.ModelSerializer):
    course=CourseSerializersWeb()
    student=StudentSerializersWeb()

    class Meta:
        model=Questions
        fields=('id','questions','student','course','slug')