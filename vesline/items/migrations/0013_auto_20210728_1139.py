# Generated by Django 3.1.5 on 2021-07-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0012_delete_itemmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(default='items/default.png', upload_to='items/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Ürünün Başlığı'),
        ),
    ]
