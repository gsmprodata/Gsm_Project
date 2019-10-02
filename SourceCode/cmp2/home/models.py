from django.db import models

class brands(models.Model):
    name = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media/logo/',default='media/default.jpg')
    def __str__(self):
        return  self.name
# class device(models.Model):
#     id = models.AutoField(primary_key=True)
class allpro(models.Model):
    # id = models.AutoField(primary_key=True)
    # idi = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    network = models.CharField(max_length=5000)
    launch = models.CharField(max_length=5000)
    body = models.CharField(max_length=5000)
    display = models.CharField(max_length=5000)
    platform = models.CharField(max_length=5000)
    memory = models.CharField(max_length=5000)
    maincamera = models.CharField(max_length=5000)
    selfiecamera = models.CharField(max_length=5000)
    sound = models.CharField(max_length=5000)
    comms = models.CharField(max_length=5000)
    features = models.CharField(max_length=5000)
    battery = models.CharField(max_length=5000)
    misc = models.CharField(max_length=5000)
    img_name = models.CharField(max_length=200,default='abc')
    head = models.CharField(max_length = 500)
    flipkart_url = models.CharField(max_length=1000)
    link_tried = models.BooleanField()
    def __str__(self):
        return  self.name
