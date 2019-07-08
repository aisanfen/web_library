from django import forms


class LoginForms(forms.Form):
    account=forms.CharField(max_length=255,min_length=1,error_messages={'required':u'用户名不能为空'})
    password=forms.CharField(max_length=255,min_length=3,error_messages={'required':u'密码不能为空'})

