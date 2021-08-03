from django import forms
from . models import Contact, Is, Staj

class ContactForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'First Name'
    }))
    last_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Last Name'
    }))
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Email'
    }))
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Your Phone'
    }))
    message = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your Message'
    }))

    class Meta:
        model = Contact
        fields =  ['first_name', 'last_name', 'email', 'phone', 'message']


class IsForm(forms.ModelForm):
    ad_soyad = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'ad soyad'
    }))
    Telefon = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Telefon'
    }))
    Ücret_Beklentiniz = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ücret Beklentiniz'
    }))
    İşe_Başlayabilme_Tarihiniz = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'İşe Başlayabilme Tarihiniz'
     }))
    Askerlik_Durumu = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Askerlik Durumu'
    }))
    Cinsiyet = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Cinsiyetiniz'
    }))
    Başvurduğunuz_Pozisyon = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Başvurduğunuz Pozisyon'
    }))
    Referanslarınız = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Referanslarınız'
    }))

    mesaj = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Mesajınız'
    }))

    class Meta:
        model = Is
        fields =  ['Askerlik_Durumu', 'Cinsiyet', 'Başvurduğunuz_Pozisyon', 'Referanslarınız', 'mesaj','Ücret_Beklentiniz','İşe_Başlayabilme_Tarihiniz','Telefon','ad_soyad',]


class StajForm(forms.ModelForm):
    Ad_Soyad = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Ad Soyad'
    }))
    Okul = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Okul'
    }))
    Bölüm = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Bölüm'
    }))
    Telefon = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Telefon'
    }))
    Yaş = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Yaş'
    }))

    class Meta:
        model = Staj
        fields =  ['Ad_Soyad', 'Okul', 'Bölüm', 'Telefon', 'Yaş']