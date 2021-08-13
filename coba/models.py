from django.db import models
from datetime import datetime, date

# Create your models here.
class Employee(models.Model):
  id = models.BigAutoField(primary_key=True)
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)

class Customer(models.Model):
  id = models.BigAutoField(primary_key=True)
  customer_name = models.CharField(max_length=255)
  city_id = models.IntegerField()
  customer_address = models.CharField(max_length=255)
  next_call_date = models.DateField(default=date.today)
  ts_inserted = models.DateTimeField(default=datetime.utcnow)

class Call(models.Model):
  id = models.BigAutoField(primary_key=True)
  employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
  customer_id = models.ForeignKey(Customer, on_delete=models.CASCADE)
  start_time = models.DateTimeField()
  end_time = models.DateTimeField()