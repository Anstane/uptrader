from django.core.management.base import BaseCommand
from app.models import MenuItem

class Command(BaseCommand):
    help = 'Создаём объекты модели.'

    def handle(self, *args, **kwargs):
        main_item1 = MenuItem.objects.create(name='Main Item 1', url='main-item1', parent=None)
        main_item2 = MenuItem.objects.create(name='Main Item 2', url='main-item2', parent=None)

        child_item1 = MenuItem.objects.create(name='Child Item 1', url='child-item1', parent=main_item1)
        child_item2 = MenuItem.objects.create(name='Child Item 2', url='child-item2', parent=main_item1)

        grandchild_item1 = MenuItem.objects.create(name='Grandchild Item 1', url='grandchild-item1', parent=child_item1)
        grandchild_item2 = MenuItem.objects.create(name='Grandchild Item 2', url='grandchild-item2', parent=child_item1)

        child_item3 = MenuItem.objects.create(name='Child Item 3', url='child-item3', parent=main_item2)
        child_item4 = MenuItem.objects.create(name='Child Item 4', url='child-item4', parent=main_item2)

        self.stdout.write(self.style.SUCCESS('Объекты меню были созданы успешно.'))
