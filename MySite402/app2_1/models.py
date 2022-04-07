from django.db import models

# Create your models here.


class Person(models.Model):
    pid = models.IntegerField();
    fullName = models.CharField(max_length=50)
    contactAddress = models.CharField(max_length=50)
    photograph = models.FileField()

    class Meta:
        ordering = ['pid']

    def __str__(self):
        return str(self.pid)+", "+self.fullName+", "+self.contactAddress+", "+str(self.photograph)


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

    class Meta:
        ordering = ['cid']

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
    # id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, help_text="Enter name of place")

    class Meta:
        ordering = ['name', '-id']
        # db_table = 'tbl_places'

    def __str__(self):
        return str(self.id)+", "+self.name

class Restaurant(models.Model):
    place = models.OneToOneField(Place, primary_key=True, on_delete=models.CASCADE,
                                 help_text="Select Location")
    name = models.CharField(max_length=50, help_text="Enter Restaurent Name ")
    momo = models.BooleanField(default=True, help_text="Serve MoMo")

    def __str__(self):
        return str(self.place)+", "+self.name+", "+str(self.momo)

# One to Many (Restaurant and Staffs)
class Staff(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    class Meta:
        ordering = ['restaurant', 'name', 'email', 'phone']
        # db_table = 'tbl_staffs'

    def __str__(self):
        return str(self.restaurant)+", "+self.name+", "+self.email+", "+self.phone


# Many to Many
class Publication(models.Model):
    title = models.CharField(max_length=50)
    class Meta:
        ordering=['title']
    def __str__(self):
        return str(self.id)+", "+self.title

class Article(models.Model):
    publication = models.ManyToManyField(Publication)
    title = models.CharField(max_length=50)
    contents = models.CharField(max_length=500)

    def __str__(self):
        return str(self.publication)+", "+self.title+", "+self.contents












