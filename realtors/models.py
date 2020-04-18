from django.db import models
from datetime import datetime

# BUG https://docs.djangoproject.com/en/3.0/ref/models/fields/#django.db.models.FileField.upload_to
# BUG The instance.id is equal to None when creating new object.
def realtor_photo_path(instance, filename):
  return f"realtors/{instance.id}/{filename}"

class Realtor(models.Model):
  name = models.CharField(max_length=200)
  photo = models.ImageField(upload_to=realtor_photo_path)
  description= models.TextField(blank=True)
  phone = models.CharField(max_length=20)
  email = models.CharField(max_length=50)
  is_mvp = models.BooleanField(default=False)
  hire_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
      return self.name
  


