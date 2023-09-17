from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class slider(models.Model):
    DISCOUNT_DEAL=(
        ('HOT DEALS','HOT DEALS'),
        ('New Arrivals','New Arrivals'),
    )
    Image=models.ImageField(upload_to='media/slider_imgs')
    
    Discount_Deal=models.CharField(choices=DISCOUNT_DEAL,max_length=100)
    
    SALE=models.IntegerField() 
    Brand_Name=models.CharField(max_length=200)
    Discount=models.IntegerField()
    Link=models.CharField(max_length=200)
    
    def __str__(self):
        return self.Brand_Name


class banner_area(models.Model):
    Image=models.ImageField(upload_to='media/banner_img')
    Discount_Deal=models.CharField(max_length=100)
    quotes=models.CharField(max_length=100)
    Discount=models.IntegerField()
    Link=models.CharField(max_length=200, null=True)

    
    
    
    def __str__(self):
        return self.quotes
    

class Main_Category(models.Model):
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Category(models.Model):
    main_category=models.ForeignKey(Main_Category, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.name +" -- " + self.main_category.name
    
class Sub_Category(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    
    def __str__(self):
        return self.category.main_category.name +" -- " + self.category.name+ " -- " + self.name
    
class Section(models.Model):
    name=models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
    
class Product(models.Model):
    total_quantity=models.IntegerField()
    availability=models.IntegerField()
    Featured_Image=models.CharField(max_length=200)
    product_name=models.CharField(max_length=100)
    price=models.IntegerField()
    Discount=models.IntegerField()
    product_Information=RichTextField()
    model_name=models.CharField(max_length=100)
    Categories=models.ForeignKey(Category,on_delete=models.CASCADE)
    Description=RichTextField()
    section=models.ForeignKey(Section,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.product_name
    

class Product_Image(models.Model):
     product=models.ForeignKey(Product,on_delete=models.CASCADE)
     Image_url=models.CharField(max_length=200)
    
class Additional_Information(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    specification=models.CharField(max_length=100)
    detail=models.CharField(max_length=200)
    


    
    
    