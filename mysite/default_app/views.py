from django.shortcuts import render
from catalog.models import Catalog 


def home(request):
    context = {
    	'page_header': 'home page title',
    	'catalog': Catalog.objects.all(),
    }
    return render(request, 'default_app/home.html', context)