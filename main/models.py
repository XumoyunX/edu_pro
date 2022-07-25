from random import choice

from django.db import models


# Create your models here.


class Team(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    job = models.CharField(max_length=250)
    tag = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Coueres_price(models.Model):
    Pul = 1
    Tekin = 2
    name = models.SmallIntegerField(choices=(
        (Pul, 'pul'),
        (Tekin, 'tekin')
    ))


    def __str__(self):
        return self.name

class Coueres(models.Model):
    coueres_price = models.ForeignKey(Coueres_price, null=True, on_delete=models.CASCADE)
    user = models.ForeignKey('client.User', null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    text = models.TextField()
    img = models.ImageField(upload_to='images/')
    course_data = models.CharField(max_length=250)
    joy_qolgan = models.CharField(max_length=50)
    video = models.FileField(upload_to='video/')



    def __str__(self):
        return self.name

class Team_bola(models.Model):
    img = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=250)
    text=models.TextField()
    job = models.TextField()
    instagram = models.CharField(max_length=250)
    github = models.CharField(max_length=250)
    fezbook = models.CharField(max_length=250)



    def __str__(self):
        return self.name