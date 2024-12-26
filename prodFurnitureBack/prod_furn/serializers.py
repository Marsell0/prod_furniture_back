from . import models
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = "__all__"

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('id', 'order_date', 'status', 'description', 'expected_completion_date')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = ('id', 'name', 'order_id_id')


class StringListSerializer(serializers.ListSerializer):
    child = serializers.CharField()

    
class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = ('id', 'name', 'quantity', 'unit_price', 'in_stock')