from django.shortcuts import render
from django.db.models import Q
from .models import Products, Size, Brands, Type, Categories
from django.views.generic import DetailView, ListView


def home(request):
    sale_product = Products.objects.filter(is_best_seller = True)
    new_arrivals = Products.objects.filter(is_new_arrivals = True)
    return render(request, "web/index.html", {'sale_product':sale_product, 'new_arrivals':new_arrivals})


class GetByAnyFilter:
    def get_by_brands(self):
        return Brands.objects.all()
    def get_by_size(self):
        return Size.objects.all()
    def get_by_type(self):
        return Type.objects.all()


class ViewMenProducts(GetByAnyFilter, ListView):
    model = Products
    queryset = Products.objects.filter(id_categories=2)


class ViewWomensProducts(GetByAnyFilter, ListView):
    model = Products
    queryset = Products.objects.filter(id_categories=3)


class ViewKidsProducts(GetByAnyFilter, ListView):
    model = Products
    queryset = Products.objects.filter(id_categories=1)


class ViewAccessoriesProducts(GetByAnyFilter, ListView):
    model = Products
    queryset = Products.objects.filter(id_type=3)


class ViewShoesProducts(GetByAnyFilter,ListView):
    model = Products
    queryset = Products.objects.filter(id_type=1)


class CatalogView(GetByAnyFilter, ListView):
    model = Products
    queryset = Products.objects.all()


class ViewDetailsProduct(DetailView):
    model = Products
    template_name = 'web/view_details_product.html'
    context_object_name = 'id'


class ViewFilterProducts(GetByAnyFilter, ListView):

    def get_queryset(self):
        queryset = Products.objects.filter(
            Q(id_brand__in=self.request.GET.getlist("brand")) |
            Q(id_type__in=self.request.GET.getlist("type")) |
            Q(size__in=self.request.GET.getlist("size"))
        )
        return queryset
