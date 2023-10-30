from django.db import models

# Create your models here.

class url_map(models.Model):
    long_url=models.URLField()
    short_url=models.CharField(max_length=6)
    
