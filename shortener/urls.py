from django.urls import re_path

from . import views

app_name = "mini_url"


urlpatterns = [
	re_path(r'^$', views.liste, name='url_liste'),
	re_path(r'^nouveau$', views.nouveau, name='url_nouveau'),
	re_path(r'^(?P<code>\w{6})/$', views.redirection,
				name='url_redirection')
 
]