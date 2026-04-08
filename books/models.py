from django.db import models

# Create your models here.

class Book(models.Model):
    #id,title, breif, image, no_of_page , price, created_at, updated_at
    title = models.CharField(max_length=255)
    brief = models.TextField()
    image = models.TextField()
    no_of_page = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
