# Generated by Django 4.2 on 2023-07-11 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0013_alter_product_created_by'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name', 'price'], 'permissions': (('create_product', 'update_product'),)},
        ),
    ]
