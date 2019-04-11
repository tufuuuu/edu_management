from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register([Student_Log_info, College, Course, Student, Teacher, Mark, Open, Term])
