from django.db import models

# Create your models here.



class product_db(models.Model):

    
    product=models.CharField(max_length=100,null=False)
    price=models.CharField(max_length=10)
    offer=models.CharField(max_length=100)
    
    brand_name=models.CharField(max_length=10)

    size_1=models.CharField(max_length=20,null=True)
    size_2=models.CharField(max_length=20,null=True)
    size_3=models.CharField(max_length=20,null=True)
    size_4=models.CharField(max_length=20,null=True)
    size_5=models.CharField(max_length=20,null=True)
    size_6=models.CharField(max_length=20,null=True)
    size_7=models.CharField(max_length=20,null=True)
    
    image1=models.ImageField(upload_to='products/',null=True,blank=True)
    image2=models.ImageField(upload_to='products/',null=True,blank=True)
    image3=models.ImageField(upload_to='products/',null=True,blank=True)
    image4=models.ImageField(upload_to='products/',null=True,blank=True)

    material=models.CharField(max_length=100,null=True)
    Heel_type=models.CharField(max_length=100,null=True)
    Water_resistance_level=models.CharField(max_length=100,null=True)
    Style=models.CharField(max_length=100,null=True)
    Outer_material=models.CharField(max_length=100,null=True)
    Country_of_Origin=models.CharField(max_length=100,null=True)

    inf1=models.CharField(max_length=200,null=True)
    inf2=models.CharField(max_length=200,null=True)
    inf3=models.CharField(max_length=200,null=True)

    

   


