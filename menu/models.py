from django.db import models
from django.urls import reverse


class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)
    menu_name = models.CharField(max_length=100)
    has_children = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.url
