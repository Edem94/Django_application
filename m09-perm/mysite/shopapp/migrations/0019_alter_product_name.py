# Generated by Django 4.2.3 on 2023-10-28 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0018_alter_order_options_alter_product_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
