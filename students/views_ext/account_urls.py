from django.contrib.auth.views import LoginView
from django.urls import path

from students.views_ext.accounts import LogoutView, RegisterView, ProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('register/', RegisterView.as_view(), name="register"),
    path('profile/', ProfileView.as_view(), name="profile"),
]