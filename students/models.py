from django.contrib.auth.models import User
from django.db import models
from django.db.models import Model


class Group(Model):
    STREAMS = [
        ("it", "Информационные технологии"),
        ("philosophy", "Философия"),
        ("ux/ui", "UX/UI"),
        ("psychology", "Психология"),
    ]

    name = models.CharField(verbose_name="Название", max_length=255)
    stream = models.CharField(verbose_name="Направление", max_length=255, choices=STREAMS)
    course = models.IntegerField(verbose_name="Курс", default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Группы"
        verbose_name = "Группа"


class Student(Model):
    name = models.CharField(verbose_name="ФИО", max_length=255)
    group = models.ForeignKey(Group, verbose_name="Группа", on_delete=models.CASCADE,
                              related_name="students")
    birthdate = models.DateField(verbose_name="Дата рождения", null=True, blank=True)
    email = models.EmailField(verbose_name="Email", null=True, blank=True)
    dropped_out = models.BooleanField(verbose_name="Отчислен", default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Студенты"
        verbose_name = "Студент"


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="ФИО")
    subject = models.CharField(max_length=255, verbose_name="Предмет")
    position = models.CharField(max_length=255, verbose_name="Должность",
                                null=True, blank=True)
    group = models.ForeignKey(Group, verbose_name="Группа", related_name="teachers",
                              on_delete=models.CASCADE)
    hired_date = models.DateField(verbose_name="Дата наема")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Учителя"
        verbose_name = "Учитель"

# Создать модель Teacher для учителя
# 1. name - ФИО
# 2. subject - предмет
# 3. position = должность (не обяз)
# 4. group - в какой группе преподает
# 5. hired_date - дата наема на работу

# Создать отдельную страницу где показаны все учителя,
# где есть кнопка "Добавить учителя"

# Страница добавления нового учителя
