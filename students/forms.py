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
