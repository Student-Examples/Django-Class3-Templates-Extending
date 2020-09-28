"""students URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from students.views import HomeView, AboutView, GroupView, AddGroupView, AddStudentView, TeachersView, AddTeacherView, \
    FeedbackView, EditGroupView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("groups/<int:group_id>/", GroupView.as_view(), name="group"),

    path("groups/<int:group_id>/edit/", EditGroupView.as_view(), name="edit_group"),

    path("groups/<int:group_id>/add-student/", AddStudentView.as_view(), name="add_student"),
    path("groups/new/", AddGroupView.as_view(), name="add_group"),
    path("about/", AboutView.as_view(), name="about"),
    path("teachers/", TeachersView.as_view(), name="teachers"),
    path("teachers/new/", AddTeacherView.as_view(), name="add_teacher"),

    path("feedback/", FeedbackView.as_view(), name="feedback"),

    path('admin/', admin.site.urls),
]
