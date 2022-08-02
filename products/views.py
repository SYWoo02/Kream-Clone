from math import ceil

import products
from .models import Product

# from . import models
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView


# Create your views here.


class ProductListView(ListView):
    model = Product
    template_name = "products/product_list"
    context_object_name = "products"
    paginate_by = 13
    ordering = ["created"]
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        context["Chloe"] = "클로이의 토이프로젝트"
        return context


# def product_list(request):
#    page = int(request.GET.get("page", 1))
#    # page_size = 10
#    # limit = page_size * page
#    # offset = limit - page_size
#    # page_count = ceil(models.Product.objects.count()/page_size)
#    # if page > page_count:
#    #    return redirect("/products")
#    product_list = Product.objects.all()
#    paginator = Paginator(product_list, 13)
#    products = paginator.get_page(page)
#
#    return render(
#        request,
#        "product_list.html",
#        {
#            "products": products,
#            "page": page,
#        },
#    )
#
