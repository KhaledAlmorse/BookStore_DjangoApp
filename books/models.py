from django.db import models

# Create your models here.


class Book(models.Model):

    title = models.CharField(max_length=255)
    brief = models.TextField()
    image = models.ImageField(upload_to="books/")
    no_of_pages = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.title}({self.id})'