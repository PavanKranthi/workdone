from django.db import models

# Create your models here.
class userlogin(models.Model):
    username=models.TextField(max_length=35,null=False,unique=True)
    password=models.TextField(max_length=20,null=False)

    def __str__(self):
        return self.username

class registerDetail(models.Model):
    username=models.TextField(max_length=35,null=False,unique=True)
    email=models.TextField(max_length=20,null=False)
    password = models.TextField(max_length=20,null=False)

    def __str__(self):
        return self.username
