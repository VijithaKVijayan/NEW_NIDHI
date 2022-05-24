import self as self
from django.db import models

# Create your models here.
# model of Employee Table
from django.db.models import F


class Employee(models.Model):

    Employee_name=models.CharField(max_length=200)
    Employee_code=models.CharField(max_length=200)
    Employee_photo=models.ImageField(upload_to='uploads/')
    Adharcard=models.FileField(upload_to='uploads/')
    Adhar_number=models.CharField(max_length=200)
    Category=models.CharField(max_length=200)
    Department=models.CharField(max_length=200)
    Designation=models.CharField(max_length=200)
    Branch=models.CharField(max_length=200)
    Employee_status=models.CharField(max_length=200)
    Date_of_joining=models.DateField()
    Reporting_to=models.CharField(max_length=200)
    Gender=models.CharField(max_length=200) 
    Guardian_name=models.CharField(max_length=200)
    Date_of_birth=models.DateField(blank=True)
    Email =models.CharField(max_length=200)
    Office_phno=models.CharField(max_length=200)
    Emergency_phno=models.CharField(max_length=200) 
    Address_pa=models.CharField(max_length=200)
    Address_ps=models.CharField(max_length=200)
    Qualification=models.CharField(max_length=200)
    Blood_Group=models.CharField(max_length=200)
    Date_of_resign=models.DateField(blank=True)
    Reason_of_Resign=models.CharField(max_length=200)
    Basic_pay=models.CharField(max_length=200)
    Daaily_Allowance=models.CharField(max_length=200)
    Other_allowance=models.CharField(max_length=200)
    Bank_name=models.CharField(max_length=200)
    Account_number=models.CharField(max_length=200)
    Ifsc_code=models.CharField(max_length=200) 
    Esi_no=models.CharField(max_length=200) 
    Pf_no=models.CharField(max_length=200)
    Welfare_no=models.CharField(max_length=200)
    def __str__(self):
        return f'{self.Employee_name}'

# DEPOSIT = (
#     ("1", "1"),
#     ("2", "2"),
#     ("3", "3"),
#     ("4", "4"),
#     ("5", "5"),
# )
TYPES = (
    ('Silver Plan', 'Silver Plan'),
    ('Diamond Plan', 'Diamond Plan'),
    ('Golden Plan', 'Golden Plan'),
    ('Royal Plan', 'Royal Plan'),
)


# model of Customer Table


# class Customer:
#     Customer_Plan = models.CharField(max_length=200, choices=TYPES)
#     Total_Amount = models.CharField(max_length=200)
#     Deposit_Year = models.IntegerField()


class Customer(models.Model):
    Username=models.CharField(max_length=222)
    Password=models.CharField(max_length=120)
    Canvassed_by=models.CharField(max_length=120)
    Customer_name=models.CharField(max_length=200)
    photo=models.ImageField(upload_to='uploads/')
    Signature=models.ImageField(upload_to='uploads/') 
    Pancard_no=models.CharField(max_length=200) 
    Adarcard_no=models.CharField(max_length=200)
    Date_of_Birth=models.CharField(max_length=200)
    Mobile_no=models.CharField(max_length=200) 
    Mobile_number1=models.CharField(max_length=200)
    Email=models.CharField(max_length=200)
    Occupation=models.CharField(max_length=200) 
    Annual_income=models.CharField(max_length=200)
    Address=models.CharField(max_length=200)
    Nominee_name=models.CharField(max_length=200) 
    Nominee_relation=models.CharField(max_length=200)
    Customer_status=models.CharField(max_length=200)
    Customer_Plan = models.CharField(max_length=200,choices = TYPES)
    Deposit_Amount = models.IntegerField(blank=True)
    Deposit_Year = models.IntegerField(blank=True)
    Anuval_stypend =models.FloatField(blank=True)
    Status=models.CharField(max_length=56,null=True,blank=True)

    def __str__(self):
         return f'{self.Customer_name}'
    #basic operation


class Admin(models.Model):
    Username=models.CharField(max_length=222)
    Password=models.CharField(max_length=120)

class LevelOne(models.Model):
    Username=models.CharField(max_length=222)
    Password=models.CharField(max_length=120)
class LevelTwo(models.Model):
    Username=models.CharField(max_length=222)
    Password=models.CharField(max_length=120)
class LevelThree(models.Model):
    Username=models.CharField(max_length=222)
    Password=models.CharField(max_length=120)


