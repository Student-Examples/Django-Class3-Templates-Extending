from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from students.models import Group


class HomeView(View):
    def dispatch(self, request, *args, **kwargs):
        groups = Group.objects.all()
        return render(request, "home.html", context={
            "header": "Peter Pen",
            "groups": groups
        })


class GroupView(TemplateView):
    template_name = "group.html"

    def get_context_data(self, **kwargs):
        group_id = kwargs["group_id"]
        group = Group.objects.get(id=group_id)
        return {
            'group': group
        }


class AddGroupView(TemplateView):
    template_name = "add_group.html"

    def dispatch(self, request, *args, **kwargs):
        error = None
        if request.method == "POST":
            name = request.POST.get("name", "")
            course = request.POST.get("course", "")
            stream = request.POST.get("stream", "")
            if name and course and stream:
                Group.objects.create(name=name, course=course, stream=stream)
                return redirect("/")
            else:
                error = "Заполните все данные"
        return render(request, self.template_name, {"error": error})


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        return {
            "header": "About page"
        }

