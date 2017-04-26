from django.shortcuts import render
from django.http import HttpResponse

def catalog_home(request):
	return HttpResponse('Catalog')

def catalog_detail(request, catalog_id):
	return HttpResponse('Catalog detail page' + catalog_id)