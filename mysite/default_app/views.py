from django.shortcuts import render
from catalog.models import Catalog 
from django.http import HttpResponse


def home(request):
    context = {
    	'page_header': 'home page title',
    	'catalog': Catalog.objects.all(),
    }
    return render(request, 'default_app/home.html', context)

def contacts(request):
	contacts_form_data = {}
	
	if request.method == 'POST':
		#contacts_form_data = request.POST
		user_name = request.POST.get('user_name')
		user_email = request.POST.get('user_email')
		message = request.POST.get('message')

		contacts_form_data.update({'user_name': user_name, 'user_email': user_email, 'message': message})
	context = {
		'page_header':'Contacts form',
		'contacts_form_data': contacts_form_data,
	}
	return render(request, 'default_app/contacts_form.html', context)