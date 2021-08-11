from django.urls import path
from .views import ItemListView, ItemDetailView
from . import views


urlpatterns = [
    path('', ItemListView.as_view(), name="items"),
    path('item/<int:pk>', ItemDetailView.as_view(), name="item_detail"),
    path('categories/<slug:category_slug>', views.category_list, name="items_by_category"),
    path('tags/<slug:tag_slug>', views.tag_list, name="tags_by_tag"),
]