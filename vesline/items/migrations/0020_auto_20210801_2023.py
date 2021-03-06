# Generated by Django 3.1.5 on 2021-08-01 17:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0019_auto_20210801_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'marka', 'verbose_name_plural': 'markalar'},
        ),
        migrations.RemoveField(
            model_name='item',
            name='fiyat',
        ),
        migrations.RemoveField(
            model_name='item',
            name='indirimsiz_fiyat',
        ),
        migrations.RemoveField(
            model_name='item',
            name='lezzeti',
        ),
        migrations.RemoveField(
            model_name='item',
            name='stok',
        ),
        migrations.RemoveField(
            model_name='item',
            name='üretim_tarihi',
        ),
        migrations.RemoveField(
            model_name='item',
            name='üretim_yeri',
        ),
        migrations.AddField(
            model_name='item',
            name='ambalaj',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ürünün ambalajı'),
        ),
        migrations.AddField(
            model_name='item',
            name='dozaj',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Ürünün dozajı'),
        ),
        migrations.AddField(
            model_name='item',
            name='renk',
            field=models.CharField(blank=True, default='beyaz', max_length=50, null=True, verbose_name='Ürünün rengi'),
        ),
        migrations.AlterField(
            model_name='item',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='items.category', verbose_name='Ürünün Markası'),
        ),
    ]
