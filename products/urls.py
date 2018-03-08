from django.urls import path
from .views import CatalogListView, ProductListView, ProductDetailView

app_name = 'products'

urlpatterns = [
    path('', CatalogListView.as_view(), name='catalogs'),
    path('<slug:catalog>/', ProductListView.as_view(), name='list'),
    path('detail/<slug:slug>', ProductDetailView.as_view(), name='detail'),
]
