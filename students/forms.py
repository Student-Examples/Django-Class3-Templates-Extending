from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.forms import ModelForm, Form
from django import forms
from students.models import Group, Student, Teacher


class GroupForm(ModelForm):
    class Meta:
        model = Group
        exclude = []
        # fields = ["name", "course", "stream"]


class StudentForm(ModelForm):
    class Meta:
        model = Student
        exclude = ["group", "dropped_out"]


class TeacherForm(ModelForm):
    class Meta:
        model = Teacher
        exclude = []


class FeedbackForm(Form):
    name = forms.CharField(label="Ваше имя", required=False)
    email = forms.EmailField(label="Ваш email")
    text = forms.CharField(label="Обратная связь", widget=forms.Textarea())


class RegisterForm(UserCreationForm):
    def clean_email(self):
        email = self.cleaned_data["email"]
        if not email.endswith("@gmail.com"):
            raise ValidationError("Only Gmail accounts is allowed")

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email")
        field_classes = {'username': UsernameField}
