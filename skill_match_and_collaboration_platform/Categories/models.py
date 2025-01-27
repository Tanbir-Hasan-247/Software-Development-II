from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, unique=True,null = True,blank=True)

    def __str__(self):
        return self.name
    