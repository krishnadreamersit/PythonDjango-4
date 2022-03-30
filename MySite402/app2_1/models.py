from django.db import models

# Create your models here.

class Person(models.Model):
    pid = models.IntegerField();
    fullName = models.CharField(max_length=50)
    contactAddress = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pid)+", "+self.fullName+", "+self.contactAddress


class Person2(models.Model):
    pid = models.IntegerField(primary_key=True);
    fullName = models.CharField(max_length=50)
    contactAddress = models.CharField(max_length=50)

    def __str__(self):
        return str(self.pid)+", "+self.fullName+", "+self.contactAddress


class Country(models.Model):
    cid = models.IntegerField(primary_key=True)
    country = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    population = models.IntegerField()
    area = models.IntegerField()

    def __str__(self):
        return str(self.cid)+", "+self.country+", "+self.region+", "+ str(self.population)+", "+str(self.area)