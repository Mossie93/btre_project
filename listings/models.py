from django.db import models
from datetime import datetime
from realtors.models import Realtor

# TODO These path-related functions seriously need to be refactored
# BUG https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.FileField.upload_to
# BUG The instance.id is equal to None when creating new object.
def listing_photo_main_path(instance, filename):
  return f"listings/{instance.id}/main-{filename}"

def listing_photo_1_path(instance, filename):
  return f"listings/{instance.id}/1-{filename}"

def listing_photo_2_path(instance, filename):
  return f"listings/{instance.id}/2-{filename}"

def listing_photo_3_path(instance, filename):
  return f"listings/{instance.id}/3-{filename}"

def listing_photo_4_path(instance, filename):
  return f"listings/{instance.id}/4-{filename}"

def listing_photo_5_path(instance, filename):
  return f"listings/{instance.id}/5-{filename}"

def listing_photo_6_path(instance, filename):
  return f"listings/{instance.id}/6-{filename}"

class Listing(models.Model):
  realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
  title = models.CharField(max_length=200)
  address = models.CharField(max_length=200)
  city = models.CharField(max_length=100)
  state = models.CharField(max_length=100)
  zipcode = models.CharField(max_length=20)
  description = models.TextField(blank=True)
  price = models.IntegerField()
  bedrooms = models.IntegerField()
  bathrooms = models.DecimalField(max_digits=2, decimal_places=1)
  garage = models.IntegerField(default=0)
  sqft = models.IntegerField()
  lot_size = models.DecimalField(max_digits=5, decimal_places=1)
  photo_main = models.ImageField(upload_to=listing_photo_main_path)
  photo_1 = models.ImageField(upload_to=listing_photo_1_path, blank=True)
  photo_2 = models.ImageField(upload_to=listing_photo_2_path, blank=True)
  photo_3 = models.ImageField(upload_to=listing_photo_3_path, blank=True)
  photo_4 = models.ImageField(upload_to=listing_photo_4_path, blank=True)
  photo_5 = models.ImageField(upload_to=listing_photo_5_path, blank=True)
  photo_6 = models.ImageField(upload_to=listing_photo_6_path, blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
      return self.title
  