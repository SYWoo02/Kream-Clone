from math import ceil

import products
from .models import Product
from . import models
from products import forms

# from . import models
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView

from django.db.models import Q


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
        # context["Chloe"] = "클로이의 토이프로젝트"
        return context


def detail(request, pk):

    try:
        product = models.Product.objects.get(id=pk)
        return render(request, "products/detail.html", {"product": product})
    except models.Product.DoesNotExist:
        return redirect("/products")
    except Exception:
        return redirect("/products")


class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context


def search(request):
    keyword = request.GET.get("keyword", None)
    price = request.GET.getlist("price", None)
    brands = request.GET.getlist("brands", None)
    form = forms.SearchForm(request.GET)
    #q = Q()
    filter_args = {}
    if form.is_valid():
        q = Q()
        if len(brands) > 0:
            filter_args["brand__pk__in"] = brands
            # models.Product.objects.filter(brand__pk__in=brands)
        if len(price) > 0:

            if "-100000" in price:
                q.add(Q(released_price__lte=100000), q.OR)

            if "100000-300000" in price:
                q.add(Q(released_price__gt=100000, released_price__lte=300000), q.OR)

            if "300000-500000" in price:
                q.add(Q(released_price__gt=300000, released_price__lte=500000), q.OR)

            if "500000-" in price:
                q.add(Q(released_price__gt=500000), q.OR)

        if keyword is not None and keyword != "":
            q.add(
                Q(eng_name__icontains=keyword)
                | Q(model_number__icontains=keyword)
                | Q(brand__name__icontains=keyword),
                q.AND,
            )
    result = models.Product.objects.filter(q, **filter_args)

    return render(
        request,
        "products/search.html",
        {"result": result, "keyword": keyword, "price": price, "form": form},
    )


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
