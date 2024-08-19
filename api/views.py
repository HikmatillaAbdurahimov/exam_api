
from rest_framework import viewsets
from .models import Teacher,Course,CourseModul,Student,StudentComment,Questions
from .serializers import TeacherSerializersWeb,CourseSerializersWeb,CourseModulSerializersWeb,StudentSerializersWeb,StudentCommentSerializerWeb,QuestionsSerializersWeb
from rest_framework.decorators import  action
from rest_framework.response import Response
from rest_framework.filters import SearchFilter



class TeacherWeb(viewsets.ModelViewSet):
    serializer_class = TeacherSerializersWeb

    def get_queryset(self):
        return Teacher.objects.all()

    """ admin qismida parametralar bo'yicha search qiladi  """
    filter_backends = [SearchFilter]
    search_fields = ['first_name','phone_number','status']


    """ o'qtuvchi darajasini suniordan middlega o'zgartiradi """
    @action(detail=False, methods=(['GET', ]))
    def junior_to_middle(self, request, *args, **kwargs):
        teachers = self.get_queryset()
        for teacher in teachers:
            teacher.junior_to_middles()
        return Response(data={'massage : junior ==> middle'})


    """ o'qtuvchi darajasini middledan juniorga o'zgartiradi  """
    @action(detail=False, methods=(['GET', ]))
    def middle_to_junior(self, request, *args, **kwargs):
        teachers = self.get_queryset()
        for teacher in teachers:
            teacher.middle_to_juniors()
        return Response(data={'middle : draft ==> junior'})


class CourseWeb(viewsets.ModelViewSet):
    serializer_class = CourseSerializersWeb

    def get_queryset(self):
        return Course.objects.all()

    """ admin qismida parametralar bo'yicha search qiladi  """
    filter_backends = [SearchFilter]
    search_fields = ['course_name','listing']

    """ action yani courseni qancha odam sotib olganini belgilaydi """
    @action(detail=True, methods=(['GET', ]))
    def listen_course(self, request, *args, **kwargs):
        course = self.get_object()
        course.listing += 1
        course.save()
        return Response(data=course.listing)



class CourseModulWeb(viewsets.ModelViewSet):
    serializer_class = CourseModulSerializersWeb

    def get_queryset(self):
        return CourseModul.objects.all()

    """ admin qismida parametralar bo'yicha search qiladi  """
    filter_backends = [SearchFilter]
    search_fields = ['course_module_name', 'course_module_name']

    """ course modulidagi ko'rishlar sonini sanaydi """
    @action(detail=True, methods=(['GET', ]))
    def listen_course_modul(self, request, *args, **kwargs):
        course = self.get_object()
        course.listing += 1
        course.save()
        return Response(data=course.listing)




class StudentWeb(viewsets.ModelViewSet):
    serializer_class = StudentSerializersWeb

    def get_queryset(self):
        return Student.objects.all()

    """ admin qismida parametralar bo'yicha search qiladi  """
    filter_backends = [SearchFilter]
    search_fields = ['last_name','first_name']

class StudentCommentWeb(viewsets.ModelViewSet):
    serializer_class = StudentCommentSerializerWeb

    def get_queryset(self):
        return StudentComment.objects.all()

    """ admin qismida parametralar bo'yicha search qiladi  """
    filter_backends = [SearchFilter]
    search_fields = ['comment','student']


    """ comentga bosilgan likelar soni  """
    @action(detail=True, methods=(['GET', ]))
    def likev_course(self, request, *args, **kwargs):
        course = self.get_object()
        course.listing += 1
        course.save()
        return Response(data=course.listing)

class QuestionsWeb(viewsets.ModelViewSet):
    serializer_class = QuestionsSerializersWeb

    def get_queryset(self):
        return Questions.objects.all()

    """ admin qismida parametralar bo'yicha search qiladi  """
    filter_backends = [SearchFilter]
    search_fields = ['questions','course']

