from django.urls import path
from cms.views import savedata
from . import views
app_name='base'

urlpatterns = [
    path ('', views.home, name='home'),
    path ('About', views.abouts, name='about'),
    path ('Resume', views.resume, name='resume'),
    path ('Contact', views.contact, name='contact'),
    path ('Gallery', views.gallery, name='gallery'),
    path ('Project', views.project, name='project'),
    path ('Admin', views.admin, name='admin'),
    path ('Admin/savedata', savedata, name='savedata'),
    path ('login', views.login, name='login'),
    path ('logout', views.logout, name='logout'),

]