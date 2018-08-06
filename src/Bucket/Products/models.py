from django.db import models
import os
import random
# Create your models here.

def get_filename_ext(filepath):
    base_name = os.path.basename(filepath)
    name , ext = os.path.splitext(base_name)
    return name , ext

def upload_image_path(instance , filename):
    new_filename = random.randint(0,39993939)
    name , ext = get_filename_ext(filename)
    final_filename = '{new_filename}{ext}'.format(new_filename=new_filename,ext=ext)
    return 'products/{new_filename}/{final_filename}'.format(new_filename=new_filename,
            final_filename=final_filename)



#Custom model managers
class ProductManager(models.Manager):
    def get_by_id(self,id):
        #Override the custom get_wueryset(0 method and return results as you want using filter or get methods
        # return self.get_queryset().filter(id=id)
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    #you can also override the default methods like all() or filter()
    # def all(self):
    #     return self.blahblahblah

class Product(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2,max_digits=20,default=39.99)
    image = models.ImageField(upload_to=upload_image_path,null=True,blank=True)
    #Winding up the custom model manager objects (or give it another name rather than objects)
    objects = ProductManager()
    def __str__(self):
        return self.title

