# Generated by Django 4.0.4 on 2022-04-28 09:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_type_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='type',
            options={'verbose_name': 'Тип товара', 'verbose_name_plural': 'Типы товаров'},
        ),
    ]