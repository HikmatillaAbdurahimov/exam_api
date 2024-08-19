from django.contrib import admin
from .models import Teacher,Course,CourseModul,Student,StudentComment,Questions
from import_export.admin import ImportExportModelAdmin


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    list_display = ('first_name','last_name','image','status')


@admin.register(Course)
class CourseAdmin(ImportExportModelAdmin):
    list_display = ('course_name','price','image','listing',)

@admin.register(CourseModul)
class CourseModulAdmin(ImportExportModelAdmin):
    list_display = ('course_module_name','description','image','create_at')


@admin.register(Student)
class StudentAdmin(ImportExportModelAdmin):
    list_display = ('image',)


@admin.register(StudentComment)
class StudentComment(ImportExportModelAdmin):
    list_display = ('comment',)


@admin.register(Questions)
class QuestionsAdmin(ImportExportModelAdmin):
    list_display = ('questions',)





