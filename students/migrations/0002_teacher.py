# Generated by Django 3.0.6 on 2020-09-25 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='ФИО')),
                ('subject', models.CharField(max_length=255, verbose_name='Предмет')),
                ('position', models.CharField(blank=True, max_length=255, null=True, verbose_name='Должность')),
                ('hired_date', models.DateField(verbose_name='Дата наема')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='students.Group', verbose_name='Группа')),
            ],
            options={
                'verbose_name': 'Учитель',
                'verbose_name_plural': 'Учителя',
            },
        ),
    ]