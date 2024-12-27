from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from django.conf import settings    
from . import serializers
from .models import *


class ClientListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        clients = Client.objects.all()
        serializer = serializers.ClientSerializer(clients, many=True)
        return Response(serializer.data)                
    

class AddClientView(APIView):

    def post(self, request):
        serializer = serializers.AddClientSerializer(data=request.data) 
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
class ClientDetailView(APIView):

    def put(self, request, pk):
        try:
            client = Client.objects.get(pk=pk)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteClientView(APIView):
    def delete(self, request, client_id):
        try:
            client = Client.objects.get(id=client_id)
            client.delete()
            return Response({"detail": "Client deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Client.DoesNotExist:
            return Response({"error": "Client not found"}, status=status.HTTP_404_NOT_FOUND)
        

class OrderListView(APIView):
    # permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.all()
        serializer = serializers.OrderSerializer(orders, many=True)
        for i in range(0 , len(serializer.data)):
            client = Client.objects.get(pk=serializer.data[i]['client_id_id'])
            client_ser = serializers.ClientSerializer(client)               
            serializer.data[i]['name'] = client_ser.data['name']    
        return Response(serializer.data)

class OrderDetailView(APIView):

    def put(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.OrderSerializer(order, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateOrderView(APIView):
    def post(self, request):
        client_name = request.data.get("client_name")
        contact = request.data.get("contact")
        description = request.data.get("description")
        
        if not client_name or not contact or not description:
            return Response({"error": "All fields are required"}, status=status.HTTP_400_BAD_REQUEST)
        
        client, _ = Client.objects.get_or_create(name=client_name, contact_info=contact)
        order = Order.objects.create(client_id=client, description=description)
        
        return Response({"detail": "Order created successfully", "order_id": order.id}, status=status.HTTP_201_CREATED)


class DeleteOrderView(APIView):
    def delete(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            order.delete()
            return Response({"detail": "Order deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
        except Client.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)


class ProjectDetailView(APIView):


    def put(self, request, pk):
        try:
            project = Project.objects.get(pk=pk)
        except Material.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MaterialListView(APIView):

    def get(self, request):
        materials = Material.objects.all()
        serializer = serializers.MaterialSerializer(materials, many=True)
        return Response(serializer.data)

class MaterialDetailView(APIView):
    
    def put(self, request, pk):
        try:
            material = Material.objects.get(pk=pk)
        except Material.DoesNotExist:
            return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.MaterialSerializer(material, data=request.data)
        if serializer.is_valid():
            # Проверяем изменение количества материала
            updated_quantity = serializer.validated_data.get("quantity", material.quantity)

            if updated_quantity <= 0:   
                serializer.validated_data["quantity"] = 0  
                serializer.validated_data["in_stock"] = False
            else:
                serializer.validated_data["in_stock"] = True

            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class ProjectListView(APIView):
    def get(self, request):
        projects = Project.objects.prefetch_related('project_materials__material').all()
        serializer = serializers.ProjectSerializer(projects, many=True)
        return Response(serializer.data)


class AddMaterialToProjectView(APIView):
    def post(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        material_id = request.data.get("material_id")
        quantity_used = request.data.get("quantity_used")

        if not material_id or not quantity_used:
            return Response({"error": "Material ID and quantity are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            material = Material.objects.get(id=material_id)
        except Material.DoesNotExist:
            return Response({"error": "Material not found"}, status=status.HTTP_404_NOT_FOUND)

        if material.quantity < int(quantity_used):
            return Response({"error": "Недостаточно" + material.name +"на складе"}, status=status.HTTP_400_BAD_REQUEST)

        material.quantity -= int(quantity_used)
        if material.quantity == 0:
            material.in_stock = False
        material.save()

        project_material, created = ProjectMaterial.objects.get_or_create(
            project=project,
            material=material,
            defaults={"quantity_used": quantity_used}
        )
        if not created:
            project_material.quantity_used += int(quantity_used)    
            project_material.save()

        total_cost = sum(
            pm.quantity_used * pm.material.unit_price
            for pm in project.project_materials.all()
        )
        project.predicted_cost = total_cost
        project.save()  

        return Response({"detail": "материал добавлен"}, status=status.HTTP_200_OK)

class RemoveMaterialFromProjectView(APIView):
    def delete(self, request, project_id, material_id):
        try:
            project_material = ProjectMaterial.objects.get(project_id=project_id, material_id=material_id)
        except ProjectMaterial.DoesNotExist:
            return Response({"error": "Нет материала в этом проекте"}, status=status.HTTP_404_NOT_FOUND)

        material = project_material.material
        if material.quantity == 0:
            material.in_stock = True
        material.quantity += project_material.quantity_used
        material.save() 

        project_material.delete()

        return Response({"detail": "материал удалён"}, status=status.HTTP_200_OK)


class UpdateProjectMaterialsView(APIView):
    def post(self, request, project_id):
        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response({"error": "Project not found"}, status=status.HTTP_404_NOT_FOUND)

        materials = request.data.get('materials', [])
        material_instances = Material.objects.filter(id__in=materials)

        # Удаляем все материалы проекта и добавляем новые
        ProjectMaterial.objects.filter(project=project).delete()
        ProjectMaterial.objects.bulk_create([
            ProjectMaterial(project=project, material=material) for material in material_instances
        ])

        return Response({"detail": "Materials updated successfully"}, status=status.HTTP_200_OK)
    
class CreateProjectFromOrderView(APIView):
    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        project_name = request.data.get('name', order.description)  # Если имя не указано, используем описание заявки
        
        project = Project.objects.create(name=project_name, order_id_id=order_id)

        return Response({"detail": "Project created successfully", "project": serializers.ProjectSerializer(project).data}, status=status.HTTP_201_CREATED)