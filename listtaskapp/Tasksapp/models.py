from django.db import models


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='Имя пользователя')
    age = models.IntegerField(verbose_name='Возраст пользователя')

    def __str__(self):
        return self.name


class Tasks(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название задачи')
    description = models.TextField()
    created_task = models.DateTimeField(auto_now_add=True, verbose_name='Время создания задачи')
    finished_task = models.BooleanField(default=False, verbose_name='Задача окончена')
    priority = models.BooleanField(default=False, verbose_name='Приоритет задачи')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class FavoriteTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Tasks, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user.name} {self.task.title}'