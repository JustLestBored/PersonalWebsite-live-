from django.forms import ModelForm 
from .models import *
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['intro1','intro2','name','facebook','github','linkedin','twitter','discord','phrase','description','degree','birthday','phone','city','age','email','htmlcheckbox','githubname',
        'cssCheckbox','javascriptCheckbox','reactCheckbox','tailwindCheckbox','pythonCheckbox','javaCheckbox','MongoDBCheckbox','nodejsCheckbox','flutterCheckbox','kotlinCheckbox','troubleshootingCheckbox','webdevCheckbox','networkCheckbox','emailCheckbox','school',
        'gradyear','school2','gradyear2','degreeDesc2','jobtitle','jobyear','companyname','JobDescri1','JobDescri2','JobDescri3','JobDescri4','roletitle','roleyear','ojtcompanyname',
        'roleDescri1','roleDescri2','roleDescri3','roleDescri4','degreeDesc','degree2','picture']
        