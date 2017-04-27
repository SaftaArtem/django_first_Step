from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Catalog
#from django.http import HttpResponse

def catalog_home(request):
    catalog_list = Catalog.objects.all()
    paginator = Paginator(catalog_list, 3) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        catalog = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        catalog = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        catalog = paginator.page(paginator.num_pages)
    context = {
    	'page_header': 'Catalog page',
    	'catalog': catalog,
    }
    return render(request, 'catalog/catalog.html', context)
	

def catalog_detail(request, catalog_id):
	catalog_item = get_object_or_404(Catalog, pk = catalog_id)
	context = {
	'page_header': catalog_item.title ,
    'catalog_item': catalog_item,
	}
	return render(request, 'catalog/catalog_detail.html', context)
	