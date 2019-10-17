from django.db import models

# Create your models here.
class std_reg(models.Model):
    Name=models.CharField(max_length=20)
    Father_Name=models.CharField(max_length=20)
    Mother_Name=models.CharField(max_length=20)
    Email=models.EmailField()
    Confirm_Email=models.EmailField()
    Mobile=models.BigIntegerField()
    Address=models.TextField(max_length=40)
    ZipCode=models.IntegerField()

class BatchTiming(models.Model):
    Batch=models.CharField(max_length=10)
    Timing=models.DateTimeField()

class Assignment(models.Model):
    Class=models.CharField(max_length=20)
    Title=models.CharField(max_length=200)
    Posted_date=models.DateField()
    Submission_Date=models.DateField()

class notification(models.Model):
    Subject=models.CharField(max_length=200)
    Posted_date=models.DateField()
