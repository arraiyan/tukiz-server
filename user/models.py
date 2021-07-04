#from typing_extensions import Required
from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.files import FileField
from django.db.models.fields.related import OneToOneField
from PIL import Image
# Create your models here.
class post(models.Model):

    user=models.ForeignKey(User,on_delete=CASCADE)
    title = models.CharField(max_length=250,default="No title")
    body=models.TextField(blank=True)
    meta_body=models.CharField(max_length=90,default="none",blank=False)
    image = models.ImageField(blank=True ,default='none.jpg')
    def __str__(self) -> str:
        return f'{self.user}and post no{self.id}'
    # def save(self):
    #     super().save()
    #     img = Image.open(self.image.path)
    #     if img.height > 150 or img.width > 300:
    #         output_size=(100,100)
    #         img.resize(output_size)
    #         img.save(self.image.path)


class postphotos(models.Model):
    user = models.ForeignKey(post,on_delete=CASCADE)
    image = models.ImageField(blank=True ,default='none.jpg')
    def __str__(self) -> str:
        return f'{self.user}and post no{self.id}'


class postbody(models.Model):
    user = models.ForeignKey(post,on_delete=CASCADE)
    body = models.TextField(default="")
    def __str__(self) -> str:
        return f'{self.user}and post no{self.id}'
class postfile(models.Model):
    user = models.ForeignKey(post,on_delete=CASCADE)
    image = models.ImageField(blank=True ,default='none.jpg')
    def __str__(self) -> str:
        return f'{self.user}and post no{self.id}'




class comment(models.Model):
    key=models.ForeignKey(post,on_delete=CASCADE)
    comment_body=models.TextField()
    comment_body_sys=models.TextField(default="")
    user = models.CharField(max_length=4,default="None")
    file=models.FileField(default='media/none.jpg',blank=True)
    is_auth = models.BooleanField(blank=False,default=False)
    def __str__(self) -> str:
        return f'post id::{self.key.id}'
    


class profile(models.Model):
    user=OneToOneField(User,on_delete=CASCADE)
    profile_image=FileField(default='media/none.jpg',blank=True)
    nick_name=CharField(default='none',max_length=50,blank=True)
    def __str__(self) -> str:
        return f'{self.user.username}...profile {self.user.id}'



