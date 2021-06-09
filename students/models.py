from django.db import models
from django.contrib.auth.models import User,AbstractUser

# Create your models here.
class Myuser(AbstractUser):
    #myfirst_name=models.CharField(max_length=100)
    def __str__(self):
        return f"{self.username} {self.last_name}"

        pass
class Records(models.Model):
    user=models.OneToOneField(Myuser, on_delete=models.CASCADE)
    maths=models.CharField(max_length=100)
    english=models.CharField(max_length=100)
    phy=models.CharField(max_length=100)
    chem=models.CharField(max_length=100)
    agric=models.CharField(max_length=100)
    bio=models.CharField(max_length=100)
    geog=models.CharField(max_length=100)
    fm=models.CharField(max_length=100)
    comp=models.CharField(max_length=100)
    Class=models.CharField(max_length=100)
    dep=models.CharField(max_length=100)
    age=models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.first_name}"


