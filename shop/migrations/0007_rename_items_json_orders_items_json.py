# Generated by Django 3.2.8 on 2021-10-10 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_rename_addreess_orders_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='items_json',
            new_name='items_Json',
        ),
    ]
