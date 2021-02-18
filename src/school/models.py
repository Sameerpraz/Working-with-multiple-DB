from django.db import models

# Create your models here.
class PreNursery(models.Model):
    name = models.CharField(max_length=50)
    class Meta:
        app_label = 'school'
