from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
 
class User (AbstractUser):
    intro1 = models.TextField(null = True, blank = True)
    intro2 = models.TextField(null = True, blank = True)
    picture = models.ImageField(upload_to='images/', null= True, blank=True)

    name = models.TextField( null = True, blank = True)
    facebook = models.TextField( null = True, blank = True)
    github = models.TextField( null = True, blank = True)
    discord = models.TextField( null = True, blank = True)
    linkedin = models.TextField( null = True, blank = True)
    twitter = models.TextField( null = True, blank = True)

    phrase = models.TextField( null = True, blank = True)
    description = models.TextField( null = True, blank = True)
    degree = models.TextField( null = True, blank = True)
    birthday = models.TextField( null = True, blank = True)
    phone = models.TextField(max_length=11, null = True, blank = True)
    city = models.TextField( null = True, blank = True)
    age = models.TextField( null = True, blank = True)
    email = models.TextField( null = True, blank = True)
    githubname = models.TextField( null = True, blank = True)

    htmlcheckbox = models.BooleanField(default=False)
    cssCheckbox = models.BooleanField(default=False)
    javascriptCheckbox = models.BooleanField(default=False)
    reactCheckbox = models.BooleanField(default=False)
    tailwindCheckbox = models.BooleanField(default=False)
    pythonCheckbox = models.BooleanField(default=False)
    javaCheckbox = models.BooleanField(default=False)
    MongoDBCheckbox = models.BooleanField(default=False)
    nodejsCheckbox = models.BooleanField(default=False)
    flutterCheckbox = models.BooleanField(default=False)
    kotlinCheckbox = models.BooleanField(default=False)

    troubleshootingCheckbox = models.BooleanField(default=False)
    webdevCheckbox = models.BooleanField(default=False)
    networkCheckbox = models.BooleanField(default=False)
    emailCheckbox = models.BooleanField(default=False)

    
    school = models.TextField( null = True, blank = True)
    gradyear = models.TextField( null = True, blank = True)
    degreeDesc = models.TextField( null = True, blank = True)
   
    degree2 = models.TextField( null = True, blank = True)
    school2 = models.TextField( null = True, blank = True)
    gradyear2 = models.TextField( null = True, blank = True)
    degreeDesc2 = models.TextField( null = True, blank = True)

    jobtitle = models.TextField( null = True, blank = True)
    jobyear = models.TextField( null = True, blank = True)
    companyname = models.TextField( null = True, blank = True)
    JobDescri1 = models.TextField( null = True, blank = True)
    JobDescri2 = models.TextField( null = True, blank = True)
    JobDescri3 = models.TextField( null = True, blank = True)
    JobDescri4 = models.TextField( null = True, blank = True)

    roletitle = models.TextField( null = True, blank = True)
    roleyear = models.TextField( null = True, blank = True)
    ojtcompanyname = models.TextField( null = True, blank = True)
    roleDescri1 = models.TextField( null = True, blank = True)
    roleDescri2 = models.TextField( null = True, blank = True)
    roleDescri3 = models.TextField( null = True, blank = True)
    roleDescri4 = models.TextField( null = True, blank = True)


    def str(self):
        return self.email or str(self.id)