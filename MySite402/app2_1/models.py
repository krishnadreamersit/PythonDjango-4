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

# Models
class Model1(models.Model):
    # automatically add id field as primary key and autoincrement
    fullName = models.CharField(max_length=50)

    class Meta:
        #ordering=['id'] # ASC
        ordering = ['-id']  # DESC
        # default table name : app2_1_Model1
        # db_table = 'tbl_persons'

    # set visibility of model in admin panel
    def __str__(self):
        return str(self.id)+", "+self.fullName

class Model2(models.Model):
    pid = models.IntegerField(primary_key=True) # User defined primary key, manually assign value
    fullName = models.CharField(max_length=50)
    contactAddress = models.CharField(max_length=50)

class Model3(models.Model):
    pass

# Models field types
# https://docs.djangoproject.com/en/4.0/ref/models/fields/

# Relationship between Models

# One to One
class Place(models.Model):
    name = models.CharField(max_length=50, help_text="Enter name of place")
    def __str__(self):
        return str(self.id)+", "+self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, primary_key=True, on_delete=models.CASCADE, help_text="Select Location")
    name = models.CharField(max_length=50, help_text="Enter Restaurent Name ")
    momo = models.BooleanField(default=True, help_text="Serve MoMo")

    def __str__(self):
        return str(self.place)+", "+self.name+", "+str(self.momo)
















