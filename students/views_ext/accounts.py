from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView

from students.forms import RegisterForm


class ProfileView(TemplateView):
    template_name = "registration/profile.html"


class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class RegisterView(TemplateView):
    template_name = "registration/register.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(reverse("home"))

        form = RegisterForm()

        if request.method == "POST":
            form = RegisterForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Вы успешно зарегились. Теперь войдите в систему")
                return redirect(reverse("login"))
        return render(request, self.template_name, {
            "form": form
        })


# Задание 2:
# 1. Создать страницу профиля
# 2. Показать там все поля пользователя: date_joined,
# username, last_name, first_name, email
# 3. Переходить на страницу профиля по клику на username
# в шапке сайта
