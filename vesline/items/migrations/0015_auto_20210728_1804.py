# Generated by Django 3.1.5 on 2021-07-28 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0014_auto_20210728_1803'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'verbose_name': 'ürün', 'verbose_name_plural': 'ürünler'},
        ),
    ]