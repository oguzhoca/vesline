from django.urls import path
from .views import AboutView, IndexView, ContactView, KvkView, MisyonView, IsbasvuruView, StajView


urlpatterns = [
    path('', IndexView.as_view(), name="index"),
    path('about/', AboutView.as_view(), name="about"),
    path('contact/', ContactView.as_view(), name="contact"),
    path('misyon/', MisyonView.as_view(), name="misyon"),
    path('kvk/', KvkView.as_view(), name="kvk"), 
    path('isform/', IsbasvuruView.as_view(), name="isform"),
    path('stajform/', StajView.as_view(), name="stajform"),   
    #path(route, view, opt(kısayol ismi))

]