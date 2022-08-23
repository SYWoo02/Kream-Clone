from math import ceil

from .models import Post, Photo
from . import models

# from . import models
from django.shortcuts import redirect, render
from django.urls import reverse
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView, DetailView


# Create your views here.


class StyleListView(ListView):
    model = Post
    template_name = "styles/style_list.html"
    context_object_name = "styles"
    paginate_by = 5
    ordering = ["created"]
    paginate_orphans = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        # context["Chloe"] = "클로이의 토이프로젝트"
        return context


def detail(request, pk):

    try:
        style = models.Post.objects.get(id=pk)
        return render(request, "styles/style_list.html", {"style": style})
    except models.Post.DoesNotExist:
        return redirect("/styles")
    except Exception:
        return redirect("/styles")


class StyleDetail(DetailView):
    model = Post
    pk_url_kwarg = "st"
    template_name = "styles/style_detail.html"
    context_object_name = "style"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["now"] = timezone.now()
        return context
