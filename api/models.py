from django.db import models
from .helpers import StatusChoices

""" o'qtuvchilarni malumotini saqlaydi """
class Teacher(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone_number=models.CharField(max_length=50)
    slug=models.SlugField(null=True,blank=True)
    image=models.URLField(null=True)
    status=models.CharField(max_length=5,choices=StatusChoices.choices,default=StatusChoices.JUNIOR)

    def __str__(self):
        return f"{self.first_name}--{self.last_name}"

    def junior_to_middles(self):
        if self.status == "ju":
            self.status = 'mi'
            self.save()

    def middle_to_juniors(self):
        if self.status == 'mi':
            self.status = 'ju'
            self.save()

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id','first_name','last_name']),
        ]


""" course haqida malumot sqalaydi """
class Course(models.Model):
    course_name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.URLField(null=True)
    slug = models.SlugField(null=True, blank=True)
    listing = models.BigIntegerField(default=0)
    teachers = models.ForeignKey(Teacher, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.course_name}"

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id','course_name','price']),
        ]

""" course moduli haqida malumot saqlaydi """
class CourseModul(models.Model):
    course_module_name=models.CharField(max_length=100)
    description=models.TextField()
    image=models.URLField(null=True)
    slug = models.SlugField(null=True, blank=True)
    listing = models.BigIntegerField(default=0)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.course_module_name}"

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id','course_module_name']),
        ]


""" student haqida malumot saqlaydi """
class Student(models.Model):
    first_name=models.CharField(max_length=100)
    last_name=models.CharField(max_length=100)
    image=models.URLField()
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}--{self.last_name}"

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id','first_name','last_name']),
        ]

"""course modeli uchun comment malumot sqlaydi """
class StudentComment(models.Model):
    comment=models.TextField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course_model=models.ForeignKey(CourseModul,on_delete=models.CASCADE)
    listing = models.BigIntegerField(default=0,null=True)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.comment}"

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id','comment']),
        ]


"""  Coursega beriladigan savollar malumotini saqlydi """
class Questions(models.Model):
    questions = models.TextField()
    student=models.ForeignKey(Student,on_delete=models.CASCADE)
    course=models.ForeignKey(Course,on_delete=models.CASCADE)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return f"{self.questions}"

    class Meta:
        ordering = ['id']
        indexes = [
            models.Index(fields=['id','questions']),
        ]



