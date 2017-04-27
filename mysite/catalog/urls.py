from django.conf.urls import url

from . import views

app_name = 'catalog'
urlpatterns = [
	url(r'^$', views.catalog_home, name="home"),
	#url(r'^(?P<catalog_id>[0-9]+)$', views.catalog_detail, name='catalog_detail'),
	url(r'^(?P<catalog_id>[\d+]+)$', views.catalog_detail, name='detail'),
]