from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    describ = models.TextField()
    image = models.ImageField(upload_to='blog_images/')
