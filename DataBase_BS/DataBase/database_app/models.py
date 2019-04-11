from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Student_Log_info(models.Model):
    user = models.CharField(max_length=30, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    student_no = models.CharField(max_length=10, primary_key=True, null=False)

class Teacher_Log_info(models.Model):
    user = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=128)
    teacher_no = models.CharField(max_length=10, unique=True)

class Admin_Log_info(models.Model):
    user = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=128)

class College(models.Model):
    number = models.CharField(max_length=5, primary_key=True, null=False)
    name = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=50, null=False, default='上海大学宝山校区')
    phone = models.CharField(max_length=15, null=False, default='00000000')

    def __str__(self):
        return self.number

class Student(models.Model):
    gender = (('male','男'),
              ('female','女'),
              )
    number = models.CharField(max_length=10, primary_key=True, null=False)
    name = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=32, choices=gender, default='男', null=False)
    birth = models.DateField(default=timezone.now, null=False)
    home_town = models.CharField(max_length=10, null=False)
    phone = models.CharField(max_length=15, default='13000000000', null=False)
    college = models.ForeignKey(College, to_field="number", on_delete=False)

    def __str__(self):
        return self.number

class Teacher(models.Model):
    gender = (('male', '男'),
              ('female', '女'),
              )
    number = models.CharField(max_length=10, primary_key=True, null=False)
    name = models.CharField(max_length=10, null=False)
    sex = models.CharField(max_length=32, choices=gender, default='男', null=False)
    birth = models.DateField(default=timezone.now, null=False)
    rank = models.CharField(max_length=10, default='讲师', null=False)
    salary = models.IntegerField(null=False, default=0)
    college = models.ForeignKey(College, to_field="number", on_delete=False)

    def __str__(self):
        return self.number

class Course(models.Model):
    number = models.CharField(max_length=8, primary_key=True, null=False)
    name = models.CharField(max_length=10, null=False)
    credit = models.IntegerField(default=0, null=False)
    class_hour = models.IntegerField(default=0, null=False)
    college = models.ForeignKey(College, to_field="number", on_delete=False)

    def __str__(self):
        return self.number

class Open(models.Model):
    term = models.CharField(max_length=15, null=False)
    c_number = models.ForeignKey(Course, to_field="number", null=False, on_delete=False)
    t_number = models.ForeignKey(Teacher, to_field="number", null=False, on_delete=False)
    time = models.CharField(max_length=10, null=False)

    class Meta:
        unique_together = (("term", "c_number", "t_number"))

class Mark(models.Model):
    s_number = models.ForeignKey(Student, to_field="number", null=False, on_delete=False)
    term = models.CharField(max_length=15, null=False)
    c_number = models.ForeignKey(Course, to_field="number", null=False, on_delete=False)
    t_number = models.ForeignKey(Teacher, to_field="number", null=False, on_delete=False)
    r_grade = models.IntegerField(null=True)
    e_grade = models.IntegerField(null=True)
    t_grade = models.IntegerField(null=True)

    class Meta:
        unique_together=(("s_number", "term", "c_number", "t_number"))

class Term(models.Model):
    term = models.CharField(max_length=15, null=False, unique=True)
