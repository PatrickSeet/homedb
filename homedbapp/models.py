from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Shopper(AbstractUser):
    phone = models.CharField(max_length=12, help_text="Format should be: 650-111-2222")

    def __unicode__(self):
        return u'{}'.format(self.username)


class Property(models.Model):
    mlsid = models.IntegerField()
    address = models.CharField(max_length=100)
    numofbdrms = models.IntegerField()
    numofbthrms = models.FloatField()
    numofmaster = models.IntegerField()
    sqfootage = models.IntegerField()
    lotsize = models.IntegerField()
    askingprice = models.IntegerField()
    offeredpricce = models.IntegerField()
    soldprice = models.IntegerField()
    propertytype = models.CharField(max_length=100)
    xcoordinate = models.FloatField(null=True)
    ycoordinate = models.FloatField(null=True)
    roof = models.CharField(max_length=100)
    kitchen  = models.CharField(max_length=100)
    bathrooms  = models.CharField(max_length=100)
    frontyard  = models.CharField(max_length=100)
    backyard  = models.CharField(max_length=100)
    termite  = models.CharField(max_length=100)
    foundation  = models.CharField(max_length=100)
    neighborhood  = models.CharField(max_length=100)
    image = models.ImageField(upload_to='prop_images', blank=True, null=True, default='prop_images/house-logo-hi.png')
    shopper = models.ManyToManyField(Shopper, related_name='shopper')

    def __unicode__(self):
        return u'{}'.format(self.address)