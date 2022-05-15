from pickle import FALSE
from tkinter import Widget
from django.conf import settings
from django.db import models


# Create your models here.

class tbl_Authentication(models.Model):
    
    loginid = models.CharField(max_length=10, primary_key = True,default='101')
    username = models.CharField(max_length=50,default='')
    password = models.CharField(max_length=50,default='')
    is_active = models.IntegerField(null=True)
    role = models.IntegerField(null = False, default='1')
    last_login = models.DateTimeField(auto_now= True)
 
    def __str__(self):
        return self.username
 
    loginauth_objects = models.Manager()



class student_data(models.Model):
    username = models.CharField(max_length=50, primary_key = True, default = '101')
    name = models.CharField(max_length = 60)
    age = models.IntegerField(null = True)
    gender = models.CharField(max_length=1)
    department = models.IntegerField(null = True)
    book1 = models.CharField(max_length=200)
    book2 = models.CharField(max_length=200)
    book3 = models.CharField(max_length=200)
    
    def __str__(self):
        return self.username
 
    Studentdata_objects = models.Manager()
    
    
class books_history(models.Model):
    stu_username = models.CharField(max_length=50)
    book1 = models.TextField()
    book2 = models.TextField()
    book3 = models.TextField()
    book1_allocatedon = models.DateField()
    book2_allocatedon  = models.DateField()
    book3_allocatedon = models.DateField()
    book1_allocatedby = models.CharField(max_length=50)
    book2_allocatedby = models.CharField(max_length=50)
    book3_allocatedby = models.CharField(max_length=50)
    
    
    def __str__(self):
        return self.stu_username
    
    
class book_history(models.Model):
    stu_username = models.CharField(max_length=50)
    book1 = models.TextField()
    book1_allocatedon = models.DateField()
    
    
class librarian_data(models.Model):
    lib_username = models.CharField(max_length=50, unique=True, primary_key= True)
    lib_name = models.CharField(max_length=50, null = False,default = 'test')
    lib_age = models.IntegerField(null = False,default = '20')
    lib_gender = models.CharField(max_length=1)
    
    
    def __str__(self):
        return self.lib_username
    
    
class books_data(models.Model):
    book_name = models.CharField(max_length = 40, unique= True)
    book_id = models.IntegerField(null = False,default = '1001',primary_key = True )
    book_author = models.CharField(max_length= 30)
    total_count = models.IntegerField(null = False, default = '10')
    description  = models.CharField(max_length = 200)
    department  = models.IntegerField(null = False)
    location = models.IntegerField(null = False)
    
    def __str__(self):
        return self.book_name
    
    
    


    

    
    
    
    
    
    
    
    
    
    
    
    
  
  
