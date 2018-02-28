from django.conf.urls import url
from . import views

app_name='picstagram'

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^create_pictures/$', views.create_pictures, name='create_pictures'),
	url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
	url(r'^logout_user/$', views.logout_user, name='logout_user'),
	url(r'^(?P<pictures_id>[0-9]+)/delete_pictures/$', views.delete_pictures, name='delete_pictures'),
	url(r'^edit/$', views.edit, name='edit'),
	]