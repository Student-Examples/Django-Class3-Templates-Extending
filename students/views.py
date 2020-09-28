from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from students.forms import GroupForm, StudentForm, TeacherForm, FeedbackForm
from students.models import Group, Teacher


def asdsadasd(request, group_id):
    return


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
        form = GroupForm()
        if request.method == "POST":
            form = GroupForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Группа успешно создана")
                messages.error(request, "Ошибка !!!!!!!!!!")
                return redirect("/")
        return render(request, self.template_name, {"form": form})


class EditGroupView(TemplateView):
    template_name = "add_group.html"

    def dispatch(self, request, *args, **kwargs):
        group_id = kwargs['group_id']
        group = Group.objects.get(id=group_id)

        form = GroupForm(instance=group)
        if request.method == "POST":
            form = GroupForm(request.POST, instance=group)
            if form.is_valid():
                form.save()
                messages.success(request, "Группа успешно изменена")
                return redirect(reverse("group", kwargs={"group_id": group_id}))

        return render(request, self.template_name, {"form": form})


class AddStudentView(TemplateView):
    template_name = "add_student.html"

    def dispatch(self, request, *args, **kwargs):
        form = StudentForm()

        group_id = kwargs["group_id"]
        group = Group.objects.get(id=group_id)

        if request.method == "POST":
            form = StudentForm(request.POST)

            if form.is_valid():
                form.instance.group = group
                form.save()
                messages.success(request, "Студент успешно создан")
                return redirect("/")
        return render(request, self.template_name, {"form": form, "group": group})


class AboutView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        return {
            "header": "About page"
        }


class TeachersView(TemplateView):
    template_name = "teachers.html"

    def get_context_data(self, **kwargs):
        teachers = Teacher.objects.all()
        return {
            "teachers": teachers
        }


class AddTeacherView(TemplateView):
    template_name = "add_teacher.html"

    def dispatch(self, request, *args, **kwargs):
        form = TeacherForm()

        if request.method == "POST":
            form = TeacherForm(request.POST)

            if form.is_valid():
                form.save()
                messages.success(request, "Учитель успешно создан")
                return redirect("/teachers/")
        return render(request, self.template_name, {"form": form})


class FeedbackView(TemplateView):
    template_name = "forms/feedback.html"

    def dispatch(self, request, *args, **kwargs):
        form = FeedbackForm()

        return render(request, self.template_name, {"form": form})