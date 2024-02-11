from django import template
from app.models import MenuItem

register = template.Library()

@register.inclusion_tag('menu.html')
def draw_menu(url=None):
    item = MenuItem.objects.get(url=url)

    def go_up(item, up_list=[]):
        if item.parent is not None:
            parent = item.parent
            children = parent.children.all()
            children_list = [child for child in children]
            up_list.extend([children_list])
            go_up(parent, up_list)
        else:
            up_list.append([item])
        
        return up_list[::-1]

    def go_down(item):
        down_list = []
        children = item.children.all()
        children_list = [child for child in children]
        if children_list:
            down_list.extend([children_list])
        return down_list

    up = go_up(item)
    down = go_down(item)
    menu = up + down

    return {'menu': menu}
