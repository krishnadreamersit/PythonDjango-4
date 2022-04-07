from django.db import models

# Create your models here.

class SiteTitle(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return str(self.id)+", "+self.title

# Banner Tilte, Content, and Image
class Banner(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    photo = models.FileField()

    def __str__(self):
        return str(self.id)+", "+self.title+", "+self.photo.url
