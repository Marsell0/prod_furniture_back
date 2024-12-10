from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from . import serializers
from .models import *
    

class ClientsAPIList(ListCreateAPIView):
    queryset = Client.objects.all()
    serializer_class = serializers.ClientSerializer
    

    

class OrderListAPIView(ListCreateAPIView):
    serializer_class = serializers.OrderSerializer

    def get_queryset(self):
        return Order.objects.all()
    

class ProjectListAPIView(ListCreateAPIView):
    serializer_class = serializers.ProjectSerializer

    def get_queryset(self):
        return Project.objects.all()
    

class MaterialListAPIView(ListCreateAPIView):
    serializer_class = serializers.MaterialSerializer

    def get_queryset(self):
        return Material.objects.all()