from django.shortcuts import render
from .models import Products
from django.views.generic import DetailView


def home(request):
    sale_product = Products.objects.filter(is_best_seller = True)
    new_arrivals = Products.objects.filter(is_new_arrivals = True)
    return render(request, "web/index.html", {'sale_product':sale_product, 'new_arrivals':new_arrivals})

class ViewDetailsProduct(DetailView):
    model = Products
    template_name = 'web/view_details_product.html'
    context_object_name = 'id'

def viewsAllCatalog(request):
    all_product =  Products.objects.all()
    return render(request, "web/catalog.html", {'all_product':all_product})


