from django.views.generic import ListView, DetailView
from .models import Product, Catalog


class CatalogListView(ListView):
    model = Catalog
    context_object_name = 'catalogs'
    template_name = 'products/catalogs.html'


class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'products/product_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(slug__catalog=self.kwargs['catalog'])
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        catalog = Catalog.objects.get(slug=self.kwargs['catalog'])
        context['catalog_name'] = catalog.title
        return context


class ProductDetailView(DetailView):
    model = Product
    context_object_name = 'product'
    template_name = 'products/product_detail.html'
