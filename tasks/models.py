from django.db import models


class Project(models.Model):

    name = models.CharField(max_length=150, verbose_name='Название проекта')
    description = models.TextField(verbose_name='Описание проекта')
    date_of_creation = models.DateField(
        auto_now=False, verbose_name='Дата создания', auto_now_add=True, editable=False)
    last_modified = models.DateField(
        auto_now=True, verbose_name='Дата обновления', editable=False)


class Task(models.Model):

    STATUS_CHOICES = [
        (0, 'Новое'),
        (1, 'В процессе'),
        (2, 'Завершено')
    ]

    title = models.CharField(max_length=150, verbose_name='Название задачи')
    description = models.TextField(verbose_name='Описание задачи')

    status = models.IntegerField(choices=STATUS_CHOICES, editable=True)

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, verbose_name='Проект')

    assignee = None

    date_of_creation = models.DateField(
        auto_now=False, verbose_name='Дата создания', auto_now_add=True, editable=False)
    last_modified = models.DateField(
        auto_now=True, verbose_name='Дата обновления', editable=False)
