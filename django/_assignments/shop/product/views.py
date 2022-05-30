from django.views.generic import TemplateView
from product.models import Product


class ProductListView(TemplateView):
    template_name = 'product/product-list.html'

    def get_context_data(self):
        return {'products': Product.objects.all()}


class ProductDetailView(TemplateView):
    template_name = 'product/product-detail.html'

    def get_context_data(self, pk):
        return {'product': Product.objects.get(pk=pk)}
