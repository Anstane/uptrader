# Generated by Django 5.0.1 on 2024-02-09 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_menuitem_parent_alter_menuitem_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menuitem',
            old_name='name',
            new_name='title',
        ),
    ]