from django.shortcuts import render

def home(request):
    menu_links = [
        {"name": "Work", "url": "#"},
        {"name": "About", "url": "#"},
        {"name": "Contact", "url": "#"},
    ]
    return render(request, 'main/base.html', {'menu_links': menu_links})
