from django.views.generic import ListView
from .models import Product, Category

class urunler(ListView):
    model = Product
    template_name = 'urunler.html'
    context_object_name = 'products'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
