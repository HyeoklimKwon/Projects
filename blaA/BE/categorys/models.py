from django.db import models

# Create your models here.

class JobCategory(models.Model) :
    job_main_code = models.CharField(primary_key=True,max_length=3)
    job_main_category = models.CharField(max_length=20)
    
    def __str__(self) :
        return self.job_main_category

class Sido(models.Model) :
    sido_code = models.CharField(primary_key=True,max_length=10)
    sido_name = models.CharField(max_length=20)
    
    
class Gugun(models.Model) :
    gugun_code = models.CharField(primary_key=True,max_length=10)
    gugun_name = models.CharField(max_length=20)

class Dong(models.Model) :
    dong_code = models.CharField(primary_key=True,max_length=10)
    sido_name = models.CharField(max_length=20)
    gugun_name = models.CharField(max_length=20)
    dong_name = models.CharField(max_length=20)
    
    