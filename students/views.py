from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


def home_page(request):
    return render(request, "home.html", context={
        "header": "Peter Pen"
    })


class HomeView(View):
    def dispatch(self, request, *args, **kwargs):
        return render(request, "home.html", context={
            "header": "Peter Pen"
        })


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        return {
            "header": "About page"
        }

