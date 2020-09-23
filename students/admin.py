from django.contrib.admin import site
from students.models import Group, Student

site.register(Group)
site.register(Student)