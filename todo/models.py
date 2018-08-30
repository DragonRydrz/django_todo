from django.db import models

# Create your models here.


class Todo(models.Model):
    completed = models.BooleanField(default=False)
    task = models.CharField(max_length=256)

    def __str__(self):
        return self.task

    def is_completed(self):
        return self.completed
