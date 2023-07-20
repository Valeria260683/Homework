from django.shortcuts import render
from django.http import HttpResponse
from .models import Page
from django.views.generic.list import ListView

def hello(request):
    return HttpResponse("Hello")


def page_view(request):
    context = {}
    context["all_pages"] = Page.objects.all()
    return render(request, "all_pages_func.html", context)


class PageListView(ListView):
    model = Page
    template_name = "all_pages_class.html"