from django.shortcuts import render

from .models import MenuItem

def index(request):
    """Загрузка базовой страницы."""

    items = MenuItem.objects.filter(parent=None)
    return render(request, 'index.html', {'items': items})

def draw_menu(request, path):
    """Логика отображения элементов меню -> получаются из url."""

    split_path = path.split('/')
    url_of_item = split_path[-1]
    return render(request, 'index.html', {'last_item': url_of_item})
