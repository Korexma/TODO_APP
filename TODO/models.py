from django.db import models
from django.urls import reverse


# Create your models here.
class Todo(models.Model):

    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    deadline = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ['deadline']

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('todo_detail', args=[str(self.id)])
