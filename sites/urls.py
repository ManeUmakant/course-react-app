from django.conf.urls import url

from sites import views


urlpatterns = [

url(r'^signup$', views.signUp, name='signUp'),
url(r'^signin$', views.signIn, name='signIn'),
url(r'^dashboard$', views.dashBoard, name='dashboard'),
url(r'^logout$', views.logOut, name='logout'),


url(r'^json_example$', views.apiExample, name='json_example'),

url(r'^class_base$', views.classBaseView.as_view(), name='class_base')



]

