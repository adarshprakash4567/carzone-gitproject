from django.db import models
from django.conf import settings
from datetime import datetime
# Create your models here.

CATEGORY_CHOICES = (
    ('S', 'Shirt'),
    ('SW', 'Sport Shoes'),
    ('OW', 'Innerswears')
)

LABEL_CHOICES = (
    ('P', 'primary'),
    ('S', 'secondary'),
    ('D', 'danger')
)
class Accessories(models.Model):
        title = models.CharField(max_length=100)
        price = models.FloatField()
        discount_price = models.FloatField(blank=True, null=True)
        category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
        label = models.CharField(choices=LABEL_CHOICES, max_length=1)
        slug = models.SlugField()
        description = models.TextField()
        accessories_photo = models.ImageField(upload_to='photos/%y/%m/%d/')

        def __str__(self):
            return self.title