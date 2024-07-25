from django.shortcuts import render

from .models import Food, Category
from django.views.generic import TemplateView, ListView, DetailView, FormView



# Create your views here.



class ProductListView(ListView):
    model = Food
    template_name = 'pages/product_list.html'
    context_object_name = 'product_list'
    queryset = Food.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context




class ProductDetailView(DetailView):
    model = Food
    template_name = 'pages/product_detail.html'
    context_object_name = 'product'


class CategoryDetailView(DetailView):
    model = Category
    template_name = 'pages/category_detail.html'
    context_object_name = 'category'







# 1) GET     - получает данные/ можно по ID
# 2) POST    - создает
# 3) DELETE  - удаляет/ по ID
# 4) PUT     - обновляет по ID
# 5) PATCH   - все обновляет