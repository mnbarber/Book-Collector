from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    bio = models.TextField(max_length=500)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class Book(models.Model):
    title = models.CharField(max_length=150)
    length = models.IntegerField(default=0)
    cover = models.CharField(max_length=500)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")

    def __str__(self):
        return self.title