from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View


class ProfileView(View):
    def dispatch(self, request, *args, **kwargs):
        return redirect(reverse("home"))



class LogoutView(View):
    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")