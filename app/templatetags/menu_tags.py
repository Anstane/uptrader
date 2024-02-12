from django import template
from app.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html')
def draw_menu(url=None):
    """
    Пользовательский тег, занимающийся выдачей пунктов меню.

    Логика работы:
    1) Делаем запрос к БД передавая уникальное значение url;
    2) Получаем все элементы, которые идут выше этого пункта меню;
    3) Проверяем, содержит ли пункт также дочерние элементы;
    4) Составляем из этого общий список, который и будет отрисоваться в шаблоне.
    """
    item = MenuItem.objects.get(url=url)

    def go_up(item, up_list=[]): # Получаем все элементы идущие выше объекта.
        if item.parent is not None:
            parent = item.parent
            children = parent.children.all()
            children_list = [child for child in children]
            up_list.extend([children_list])
            go_up(parent, up_list)
        else:
            up_list.append([item])
        
        return up_list[::-1]

    def go_down(item): # Получаем дочерние объекты.
        down_list = []
        children = item.children.all()
        children_list = [child for child in children]
        if children_list:
            down_list.extend([children_list])
        return down_list

    up = go_up(item)
    down = go_down(item)
    menu = up + down # Складываем верхнюю часть и нижнюю для получения общего списка.

    return {'menu': menu}

# Требуется следующая доработка:
# В данный момент мы получаем списки элементов, подходящие под условия запроса.
# Нужно сделать так, чтобы у нас появилась переменная, которая будет сохранять в себе активное состояние объекта.
# В зависимости от этого состояния будет происходить запрос всех остальных элементов.

# Также нужно сделать так, чтобы остальные элементы отображались чётко по родительским.
