from django.db import models

# Create your models here.
class shop(models.Model):
    good_id = models.IntegerField(default=0)
    sell_time = models.DateTimeField()
    sell_price = models.IntegerField(default=0)
    deal_price = models.IntegerField(default=0)
