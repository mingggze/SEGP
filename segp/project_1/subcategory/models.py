from django.db import models

# Create your models here.
class subcategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=500)
    trend_score = models.DecimalField(max_digits=10, decimal_places=2)
    last_update = models.DateField(null=True, blank=True)