from django.db import models
from django.urls import reverse

# Create your models here.

PRIORITIES = (
    ('adanger', 'Priority High'),
    ('bwarning', 'Priority Medium'),
    ('csuccess', 'Priority Low')
)


class Task(models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    # username = models.ForeignKey('Username', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=1000, blank=True)
    date_of_creation = models.DateTimeField(auto_now_add=True)
    priority = models.CharField(
        max_length=30,
        choices=PRIORITIES,
        default=PRIORITIES[0][0]
    )
    complete = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)])


