from django.shortcuts import render, get_object_or_404
from .models import Catalog
#from django.http import HttpResponse

def catalog_home(request):
	context = {
	'page_header': 'catalog page title',
    'catalog': Catalog.objects.all(),
	}
	return render(request, 'catalog/catalog.html', context)
	#return HttpResponse('Catalog')

def catalog_detail(request, catalog_id):
	catalog_item = get_object_or_404(Catalog, pk = catalog_id)
	context = {
	'page_header': catalog_item.title ,
    'catalog_item': catalog_item,
	}
	return render(request, 'catalog/catalog_detail.html', context)
	#return HttpResponse('Catalog detail page' + catalog_id)