from django.db import models
from django.utils import timezone
# Create your models here.
 
class Shop(models.Model) :
    SHOP_TYPES = [
        ('SR', 'SHIRT'),
        ('PT', 'PANT'),
        ('SH', 'SHOES'),
        ('GL', 'GLASS'),
    ]
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='shops/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=SHOP_TYPES)
    description = models.TextField(default="")

    def __str__(self) -> str:
        return self.name
