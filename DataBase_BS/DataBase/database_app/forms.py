from django import forms

class UserForm(forms.Form):   #login的表单类
    username = forms.CharField(label='用户名', max_length=30)
    password = forms.CharField(label='密码', max_length=30, widget=forms.PasswordInput)

class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=30)
    password1 = forms.CharField(label='密码', max_length=128, widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码', max_length=128, widget=forms.PasswordInput)
    No = forms.CharField(label='学号', max_length=10)