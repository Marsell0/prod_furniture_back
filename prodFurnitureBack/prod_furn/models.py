from django.db import models
import datetime

class Client(models.Model):
    name = models.CharField(max_length=60)
    contact_info = models.CharField(max_length=30)
    company_name = models.CharField(max_length=60, null=True, blank=True)
    registration_date = models.DateField(default=datetime.date.today().isoformat())


class Order(models.Model):
    client_id = models.ForeignKey(Client, on_delete=models.CASCADE)
    order_date = models.DateField(default=datetime.date.today().isoformat())
    status = models.CharField(max_length=15, default='На рассмотрении', blank=True)
    description = models.TextField(null=True, blank=True)
    expected_completion_date = models.DateField(null=True, blank=True)  


class Project(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)
    name = models.CharField(max_length=60)
    specification = models.CharField(max_length=60)
    predicted_cost = models.FloatField()
    completion_deadline = models.DateField()
    status =  models.CharField(max_length=15, default='В обработке', blank=True)    


class Material(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    unit_price = models.FloatField()
    in_stock = models.BooleanField()
    

class ProjectMaterial(models.Model):
    project_id = models.ManyToManyField(Project)
    material_id = models.ManyToManyField(Material)
    quantity_used = models.IntegerField()