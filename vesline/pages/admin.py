from django.contrib import admin
from . models import Contact, Is, Staj

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):    
    list_display = ('message',)
    list_filter = ('message',)
    search_fields = ('message',)

@admin.register(Is)
class IsAdmin(admin.ModelAdmin):    
    list_display = ('ad_soyad',)
    list_filter = ('ad_soyad',)
    search_fields = ('ad_soyad',)

@admin.register(Staj)
class StajAdmin(admin.ModelAdmin):    
    list_display = ('Okul',)
    list_filter = ('Okul',)
    search_fields = ('Okul',)