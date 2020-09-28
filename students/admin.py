from django.contrib.admin import site
from students.models import Group, Student, Teacher

site.register(Group)
site.register(Student)
site.register(Teacher)