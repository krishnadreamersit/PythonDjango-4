from django.db import models


class Model1(models.Model):
    id = models.IntegerField(help_text='ID : ', primary_key=True)
    name = models.CharField(help_text="NAME : ", max_length=50)
    address = models.CharField(help_text="ADDRESS : ", max_length=50)

    class Meta:
        ordering=['id']

    def __str__(self):
        return str(self.id)+", "+self.name+", "+self.address

