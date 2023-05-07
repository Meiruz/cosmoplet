from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    about = models.CharField(max_length=250)
    image = models.ImageField(upload_to="Articles/images/")
    text = models.TextField()
    slider1 = models.ImageField(blank=True, upload_to="Articles/images/")
    slider2 = models.ImageField(blank=True, upload_to="Articles/images/")
    slider3 = models.ImageField(blank=True, upload_to="Articles/images/")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
