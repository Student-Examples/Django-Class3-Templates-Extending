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
