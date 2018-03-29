from django.conf.urls import url

from employee import views


urlpatterns = [

url(r'^hello$', views.helloDjango, name='something'),
url(r'^static_example$', views.staticExample, name='static_example'),
url(r'^hello_python$', views.helloPython, name='helloPython'),
url(r'^form_example$', views.formTest, name='form_example'),
url(r'^create$', views.create, name='create'),
url(r'^index$', views.index, name='index'),
url(r'^update/(?P<pk>[0-9]+)$', views.update, name='update'),
url(r'^delete/(?P<pk>[0-9]+)$', views.delete, name='delete'),
url(r'^view/(?P<pk>[0-9]+)$', views.view, name='view'),


url(r'^create_tech$', views.create_tech, name='create_tech'),
url(r'^index_tech$', views.index_tech, name='index_tech'),

]

