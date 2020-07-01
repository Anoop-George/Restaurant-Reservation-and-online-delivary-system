from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.conf import settings
from PIL import Image


class Tables(models.Model):

    tablerequiretime = models.CharField(max_length=200)
    tablerequireDate = models.DateField()
    created = models.DateField(auto_now=True)
    updatedat = models.DateField(auto_now_add=True)
    foodliketoeat = models.CharField(max_length=200)
    totalpersons = models.PositiveIntegerField(
        default=0, validators=[MinValueValidator(0), MaxValueValidator(20)])
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.author.username


class Product(models.Model):

    catagory_choice = [('SOUPS', 'SOUPS'), ('SOFT_BEV', 'SOFT_BEV'), ('MOCKTAIL', 'MOCKTAIL'), (
        'SALAD', 'SALAD'), ('STARTERS', 'STARTERS'), ('STARTERS_NONVEG', 'STARTERS_NONVEG'), ('SHARING', 'SHARING')]

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    image = models.ImageField(upload_to='images', blank=True, null=True)
    importance = models.BooleanField(default=False)
    data = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    catagory=models.CharField(max_length=100,choices=catagory_choice,default='SOUPS')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.image:
            pic = Image.open(self.image.path)
            if pic.height > 150 or pic.width > 150:
                output_size = (300, 300)
                pic.thumbnail(output_size)
                pic.save(self.image.path)
            super(Product, self).save(*args, **kwargs)


class PO(models.Model):

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    #image = models.ImageField(upload_to='images', blank=True, null=True)
    #importance = models.BooleanField(default=False)
    data = models.TextField(blank=True, null=True)
    quantity = models.IntegerField(default=1)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    paymentmethod = models.CharField(
        default='cash on delivary', max_length=100)
    created = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)
    rejected = models.BooleanField(default=False)
    rejected_reason = models.BooleanField(default=False)
