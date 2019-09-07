from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=300)
    pub_date = models.DateField()
    describ = models.TextField()
    image = models.ImageField(upload_to='blog_images/')


    def __str__(self):
        return self.title

    def summary(self):
        return self.describ[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d %b %Y")
