from django.db import models
from django.core.validators import RegexValidator



# Create your models here.
class Signup(models.Model):
    fname = models.CharField(max_length=50)
    number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    rollno = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    Branch = models.CharField(max_length=50)
    rt_number = models.CharField(max_length=10, validators=[RegexValidator(r'^\d{1,10}$')])
    st_name = models.CharField(max_length=50) 
    
    def __str__(self):
        return self.fname


class Contacts(models.Model):
    name = models.CharField(max_length=120)
    Hallticket = models.CharField(max_length=10)
    email = models.EmailField(max_length=254)
    desc = models.TextField(max_length=10000)
    
    def __str__(self):
        return self.name 
    
class Update(models.Model):
    descrip = models.TextField(max_length=10000)