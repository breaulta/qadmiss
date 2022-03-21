from django.db import models

# Create your models here.
class Admiss_app(models.Model):
	first_name = models.CharField(max_length=200)
	middle_name = models.CharField(max_length=200)
	last_name = models.CharField(max_length=200)
