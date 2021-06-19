from django.db import models

# Create your models here.
class details(models.Model):
    name = models.CharField(max_length=30)
    food_pic = models.ImageField(upload_to="media")
    vendor_name = models.CharField(max_length=50)
    specality = models.CharField(max_length=50)
    description = models.TextField()
    address1 = models.CharField(max_length=50)
    district = models.CharField(max_length=20, blank=False)
    phoneno = models.CharField(max_length=10)

    def __str__(self):
        return self.name + " " + self.vendor_name