from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.catalog_home, name="catalog_home"),
	#url(r'^(?P<catalog_id>[0-9]+)$', views.catalog_detail, name='catalog_detail'),
	url(r'^(?P<catalog_id>[\d+]+)$', views.catalog_detail, name='catalog_detail'),
]