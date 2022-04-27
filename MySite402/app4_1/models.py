from django.db import models


class Person(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.id)+", "+self.name+", "+self.address
