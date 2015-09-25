from django.shortcuts import render

def index(request):
	context_dict = {name: 'wlbf'}
        return render(request, 'wlbf/index.html', context_dict)
