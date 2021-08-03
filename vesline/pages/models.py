from django.db import models

# Create your models here.
from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)

    def __str__(self):
        return self.email

    
    class Meta:
        verbose_name= 'Gelen Mesaj'
        verbose_name_plural= 'Gelen Mesajlar'


class Is(models.Model):
    ad_soyad = models.CharField(max_length=100)
    Telefon = models.CharField(max_length=100)
    Ücret_Beklentiniz = models.CharField(max_length=100)
    İşe_Başlayabilme_Tarihiniz = models.CharField(max_length=100)
    Askerlik_Durumu = models.CharField(max_length=100)
    Cinsiyet = models.CharField(max_length=100)
    Başvurduğunuz_Pozisyon = models.CharField(max_length=100)
    Referanslarınız = models.TextField(blank=False, null=False)
    mesaj = models.TextField(blank=True)

    def __str__(self):
        return self.ad_soyad
    
    
    class Meta:
        verbose_name= 'iş başvurusu'
        verbose_name_plural= 'iş başvuruları'

class Staj(models.Model):
    Ad_Soyad = models.CharField(max_length=100)
    Okul = models.CharField(max_length=100)
    Bölüm = models.CharField(max_length=100)
    Telefon = models.CharField(max_length=100)
    Yaş = models.CharField(max_length=100)

    def __str__(self):
        return self.Ad_Soyad
    
    
    class Meta:
        verbose_name= 'staj başvurusu'
        verbose_name_plural= 'staj başvuruları'
