from django.shortcuts import render



def home(request):
    context = {
    	'title': 'home page title',
    }
    return render(request, 'default_app/home.html', context)