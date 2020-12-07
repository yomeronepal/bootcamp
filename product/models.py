from django.db import models

# Create your models here.

class Product(models.Model):
    CHOICES = {
        ('Black','Black'),
        ('Red','Red')
        }
    SIZES = {
        ('S','Small'),
        ('L','Large'),
        ('M','Medium'),
        ('XL','Extra Large'),
        ('2XL','Double XL')
        }
   
    name = models.CharField(max_length=40)
    price = models.IntegerField(default =0,null= True )
    color = models.CharField(max_length=20, choices = CHOICES,null= True)
    size = models.CharField(max_length=20,choices =SIZES,null = True)
    main_image = models.ImageField(upload_to='cloth_main_photo',null=True)
    description = models.TextField(max_length=1000 ,null= True)

    def __str__(self):
        return self.name