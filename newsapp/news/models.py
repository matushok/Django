from django.db import models

# Create your models here.
import datetime as dt

class Article(models.Model):

    name = models.CharField(max_length=150)

    content = models.TextField()

    image = models.ImageField()

    category = models.ForeignKey('categories.Category', on_delete=models.CASCADE)

    publicated = models.DateTimeField(null=True, blank=True, default=dt.datetime.now)

    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):

        return self.name

    @property
    def is_publicated(self):

        return bool(self.publicated)