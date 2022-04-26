from django.db import models


class Model1(models.Model):
    id = models.IntegerField(help_text='ID : ', primary_key=True)
    name = models.CharField(help_text="NAME : ", max_length=50)
    address = models.CharField(help_text="ADDRESS : ", max_length=50)

    class Meta:
        ordering=['id']

    def __str__(self):
        return str(self.id)+", "+self.name+", "+self.address


# News Model
class Model2(models.Model):
    nid = models.IntegerField(help_text="ID", primary_key=True)
    title = models.CharField(help_text="TITLE", max_length=100)
    content = models.CharField(help_text="CONTENTS", max_length=5000)

    def __str__(self):
        return str(self.nid)+", "+self.title+", "+self.content