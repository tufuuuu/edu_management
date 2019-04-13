from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict
#from database_app.models import Student_Log_info    #注入学生信息models
#from database_app.models import Admin_Log_info      #注入管理员信息models
#from database_app.models import Teacher_Log_info    #注入教师信息models
#rom database_app.models import Mark
from .models import  *
from database_app.forms import UserForm   #注入用户表单
from database_app.forms import RegisterForm  #注入注册表单
import json
import hashlib


def Index(request):
    if not request.session.get('is_login', None):
        return redirect('/login')
    message = "欢迎：" + request.session.get('user_name')
    return render(request, 'index.html', {'user':message})

def getJson(request):
    resp = {'errorcode':100,'detail':'Get success'}
    return HttpResponse(json.dumps(resp), content_type='application/json')
# Create your views here.

#hash算法加密
def hash_code(s, salt = 'mystery'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()

#学生登陆部分
def login(request):
    if request.session.get('is_login', None):
        return redirect('/index')

    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写内容"
        if login_form.is_valid():    #确保都不为空
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            #其他验证
            try:
                user_log = Student_Log_info.objects.get(user=username)
                if user_log.password == hash_code(password):
                    request.session['is_login'] = True
                    request.session['user_id'] = user_log.student_no
                    request.session['user_name'] = user_log.user
                    request.session['user_type'] = "student"
                    return redirect('/index/')
                else:
                    message = "密码不正确"
            except:
                message = "用户名不存在"
        return render(request, 'login.html', locals())

    login_form = UserForm()
    return render(request,'login.html',locals())

#登出部分
def logout(request):
    if not request.session.get('is_login',None):
        return redirect("/login/")
    request.session.flush()    #清除所有session
    return redirect('/login/')

#学生账号注册部分
def register(request):
    if request.session.get('is_login', None):
        message = "请退出以后再重新注册"
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "请检查填写的内容"
        if register_form.is_valid():
            username = register_form.cleaned_data['username']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            number = register_form.cleaned_data['No']
            if password1 != password2:
                mesaage = "两次输入的密码不同"
                return render(request, 'register.html', locals())
            else:
                same_name_user = Student_Log_info.objects.filter(user=username)
                if same_name_user:
                    message = "用户已存在，请直接登陆"
                    return render(request, 'register.html', locals())
                same_no = Student_Log_info.objects.filter(student_no=number)
                if same_no:
                    message = "该学号已注册，请直接登陆"
                    return render(request, 'register.html', locals())
                #没有重复的账号名与姓名
                Student_Log_info.objects.create( user=username, password=hash_code(password1), student_no=number)
                return redirect('/login/')
    register_form = RegisterForm()
    return render(request, 'register.html', locals())

#暂时无用
def admin(request):
    pass
    return render(request,'admin.html')

#学生成绩查询
def search_score(request, select_term):
    #验证是否登陆
    if not request.session.get('is_login', None):
        return redirect('/login/')
    #验证是否为学生
    if request.session.get('user_type') != "student":
        return redirect('/login/')

    #得到学生学号
    student_no = request.session.get('user_id')
    #将学期列表准备好
    term_list = Term.objects.all()

    #寻找学期
    if select_term:
        if select_term == "all":    #所有学期
            student = Mark.objects.filter(s_number=student_no).values()
            return render(request, "score.html", {"student_list": student, "term_list": term_list, "dropbox": "请选择学期"})
        term = Term.objects.filter(term=select_term)
        if term:                    #如果所选学期在学期表内，则寻找这个学生在这个学期内的成绩
            student = Mark.objects.filter(s_number=student_no, term=select_term).values()
            return render(request, "score.html", {"student_list": student, "term_list": term_list, "dropbox": select_term})
        message = "请选择正确的学期"            #GET方式，防止有人随便在url中加入奇怪的字符
        return render(request, "score.html", {"message": message, "term_list": term_list, "dropbox": "请选择学期"})
    return render(request, "score.html", {"term_list": term_list, "dropbox": "请选择学期"})

#学生查询课表
def search_course(request, select_term):
    # 验证是否登陆
    if not request.session.get('is_login', None):
        return redirect('/login/')
    # 验证是否为学生
    if request.session.get('user_type') != "student":
        return redirect('/login/')

    # 得到学生学号
    student_no = request.session.get('user_id')
    # 将学期列表准备好
    term_list = Term.objects.all()

    # 寻找学期
    if select_term:
        term = Term.objects.filter(term=select_term)
        if term:  # 如果所选学期在学期表内，则寻找这个学生在这个学期内的成绩
            student = Mark.objects.filter(s_number=student_no, term=select_term).values()
            for d in student:
                d['time'] = Open.objects.filter(c_number_id=d['c_number_id'], term=d['term']).values('time')[0]['time']
                d['t_name'] = Open.objects.filter()
            return render(request, "course.html",
                          {"student_list": student, "term_list": term_list, "dropbox": select_term})
        message = "请选择正确的学期"  # GET方式，防止有人随便在url中加入奇怪的字符
        return render(request, "course.html", {"message": message, "term_list": term_list, "dropbox": "请选择学期"})
    return render(request, "course.html", {"term_list": term_list, "dropbox": "请选择学期"})

#学生选课
def choose_course(request):
    # 验证是否登陆
    if not request.session.get('is_login', None):
        return redirect('/login/')
    # 验证是否为学生
    if request.session.get('user_type') != "student":
        return redirect('/login/')

    # 得到学生学号
    student_no = request.session.get('user_id')
    course_list = Open.objects.all().values()

    if request.method == "POST":
        select_course_id = request.POST.get("select_button", None)
        select_course1 = Open.objects.get(id=select_course_id)
        select_course = model_to_dict(select_course1)
        Mark.objects.create(s_number_id=student_no, term=select_course['term'], c_number_id=select_course['c_number'], t_number_id=select_course['t_number'], r_grade=0, e_grade=0, t_grade=0)

    student = Mark.objects.filter(s_number=student_no).values()
    for course in course_list:
        course['select'] = 0
        course['c_name'] = Course.objects.filter(number=course['c_number_id']).values('name')[0]['name']
        course['hour'] = Course.objects.filter(number=course['c_number_id']).values('class_hour')[0]['class_hour']
        course['credit'] = Course.objects.filter(number=course['c_number_id']).values('credit')[0]['credit']
        course['t_name'] = Teacher.objects.filter(number=course['t_number_id']).values('name')[0]['name']
        course['college'] = Course.objects.filter(number=course['c_number_id']).values('college')[0]['college']
        course['college_name'] = College.objects.filter(number=course['college']).values('name')[0]['name']
        for student_course in student:
            if course['c_number_id'] == student_course['c_number_id']:
                course['select'] = 1
                break
    return render(request, 'choose_course.html', {"courst_list": course_list})
