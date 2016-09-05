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
    numofbdrms = models.IntegerField(null=True, blank=True)
    numofbthrms = models.FloatField(null=True, blank=True)
    numofmaster = models.IntegerField(null=True, blank=True)
    sqfootage = models.IntegerField(null=True, blank=True)
    lotsize = models.IntegerField(null=True, blank=True)
    askingprice = models.IntegerField(null=True, blank=True)
    offeredpricce = models.IntegerField(null=True, blank=True)
    soldprice = models.IntegerField(null=True, blank=True)
    propertytype = models.CharField(max_length=100, blank=True)
    xcoordinate = models.FloatField(null=True, blank=True)
    ycoordinate = models.FloatField(null=True, blank=True)
    roof = models.CharField(max_length=100, null=True, blank=True)
    kitchen  = models.CharField(max_length=100, null=True, blank=True)
    bathrooms  = models.CharField(max_length=100, null=True, blank=True)
    frontyard  = models.CharField(max_length=100, null=True, blank=True)
    backyard  = models.CharField(max_length=100, null=True, blank=True)
    termite  = models.CharField(max_length=100, null=True, blank=True)
    foundation  = models.CharField(max_length=100, null=True, blank=True)
    neighborhood  = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='prop_images', blank=True, null=True, default='prop_images/house-logo-hi.png')
    shopper = models.ManyToManyField(Shopper, related_name='shopper')

    def __unicode__(self):
        return u'{}'.format(self.address)