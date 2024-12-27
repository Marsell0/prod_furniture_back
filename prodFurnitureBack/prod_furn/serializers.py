from . import models
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = "__all__"

class AddClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Client
        fields = ('name', 'contact_info')


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Employee
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = ('id', 'order_date', 'status', 'description', 'expected_completion_date', 'client_id_id')


class MaterialSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Material
        fields = ['id', 'name', 'quantity', 'unit_price', 'in_stock']

class ProjectMaterialSerializer(serializers.ModelSerializer):
    material = MaterialSerializer()
    total_price = serializers.SerializerMethodField()

    class Meta:
        model = models.ProjectMaterial
        fields = ['id', 'material', 'quantity_used', 'total_price']

    def get_total_price(self, obj):
        return obj.quantity_used * obj.material.unit_price

class ProjectSerializer(serializers.ModelSerializer):
    project_materials = ProjectMaterialSerializer(many=True, read_only=True)

    class Meta:
        model = models.Project
        fields = ['id', 'name', 'specification', 'project_materials', 'predicted_cost']

    def get_total_cost(self, obj):
        return sum(pm.total_price() for pm in obj.project_materials.all())