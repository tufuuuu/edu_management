from django.db import models
import django.utils.timezone as timezone


# Create your models here.
class Student_Log_info(models.Model):
    user = models.CharField(max_length=30, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)
    student_no = models.CharField(max_length=10, primary_key=True, null=False)
    class Meta():
        verbose_name_plural='学生登陆信息'

class Teacher_Log_info(models.Model):
    user = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=128)
    teacher_no = models.CharField(max_length=10, unique=True)
    class Meta():
        verbose_name_plural='教师登陆信息'

class Admin_Log_info(models.Model):
    user = models.CharField(max_length=30, primary_key=True)
    password = models.CharField(max_length=128)

class College(models.Model):
    number = models.CharField(max_length=5, primary_key=True, null=False)
    name = models.CharField(max_length=20, null=False)
    location = models.CharField(max_length=50, null=False, default='上海大学宝山校区')
    phone = models.CharField(max_length=15, null=False, default='00000000')

    def __str__(self):
        return "{0} - {1}".format(self.number, self.name)
    class Meta():
        verbose_name_plural='学院信息'

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
    class Meta():
        verbose_name_plural='学生详细信息'

    def __str__(self):
        return "{0} - {1}".format(self.number, self.name)

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
    class Meta():
        verbose_name_plural='教师详细信息'

    def __str__(self):
        return "{0} - {1}".format(self.number, self.name)

class Course(models.Model):
    number = models.CharField(max_length=8, primary_key=True, null=False)
    name = models.CharField(max_length=10, null=False)
    credit = models.IntegerField(default=0, null=False)
    class_hour = models.IntegerField(default=0, null=False)
    college = models.ForeignKey(College, to_field="number", on_delete=False)
    class Meta():
        verbose_name_plural='课程信息'

    def __str__(self):
        return "{0} - {1}".format(self.number, self.name)

class Open(models.Model):
    term = models.CharField(max_length=15, null=False)
    c_number = models.ForeignKey(Course, to_field="number", null=False, on_delete=False)
    t_number = models.ForeignKey(Teacher, to_field="number", null=False, on_delete=False)
    time = models.CharField(max_length=10, null=False)
    al_sel = models.IntegerField(null=False, default=0)
    volume = models.IntegerField(null=False, default=50)
    #class Meta():
        #verbose_name_plural='开课情况'
    class Meta():
        unique_together = (("term", "c_number", "t_number"))
        verbose_name_plural = '开课情况'

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.term, self.c_number, self.t_number, self.time)

class Mark(models.Model):
    s_number = models.ForeignKey(Student, to_field="number", null=False, on_delete=False)
    term = models.CharField(max_length=15, null=False)
    c_number = models.ForeignKey(Course, to_field="number", null=False, on_delete=False)
    t_number = models.ForeignKey(Teacher, to_field="number", null=False, on_delete=False)
    r_grade = models.IntegerField(null=True)
    e_grade = models.IntegerField(null=True)
    t_grade = models.IntegerField(null=True)

    class Meta():
        unique_together=(("s_number", "term", "c_number", "t_number"))
        verbose_name_plural='成绩管理'

    def __str__(self):
        return "{0} - {1} - {2} - {3}".format(self.s_number, self.c_number, self.t_number, self.term)

class Term(models.Model):
    term = models.CharField(max_length=15, null=False, unique=True)
    class Meta():
        verbose_name_plural='学期表'

    def __str__(self):
        return self.term

class Term_Open(models.Model):
    status = (('open', 'open'),
              ('close', 'close'))
    now_term = models.ForeignKey(Term, to_field="term", null=False, on_delete=False)
    open = models.CharField(max_length=32, choices=status, default='open', null=False)
    class Meta():
        verbose_name_plural='当前学期与选课时间管理'

    def __str__(self):
        return "{0} - {1}".format(self.now_term, self.open)


