from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from .models import *
    

class ClientsAPIList(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    

class OrderListView(APIView):
    def get(self, request):
        orders = Order.objects.all()
        serializer = serializers.OrderSerializer(orders, many=True)
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
    

class ProjectListAPIView(ListCreateAPIView):
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()
    

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
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)