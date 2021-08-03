from django.db import models
from django.db.models.base import Model


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name= 'marka'
        verbose_name_plural= 'markalar'

class Tag(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(max_length=50, unique=True, null=True)

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=50, verbose_name="Ürünün Adı")
    dozaj = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ürünün dozajı")
    renk = models.CharField(max_length=50,blank=True, null=True, default='beyaz', verbose_name="Ürünün rengi")
    title = models.CharField(max_length=50, verbose_name="Ürünün Başlığı")
    ambalaj = models.CharField(max_length=50, blank=True, null=True, verbose_name="Ürünün ambalajı")
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING, verbose_name="Ürünün Markası")
    tags = models.ManyToManyField(Tag, blank=True)
    image = models.ImageField(upload_to="items/%Y/%m/%d/", default="/media/default.png")
    description = models.TextField(blank=True, verbose_name="Ürün Açıklaması")


    
    class Meta:
        verbose_name= 'ürün'
        verbose_name_plural= 'ürünler'
    

