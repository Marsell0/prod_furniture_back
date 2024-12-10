from django.urls import path
from . import api

urlpatterns = [
    path('clients/', api.ClientsAPIList.as_view(), name='get_all_clients'),
    path('clients/<int:client_id>', api.ClientsAPIList.as_view(), name='get_client_by_id'),
    path('orders', api.OrderListAPIView.as_view(), name='api_orders'),
    path('projects', api.ProjectListAPIView.as_view(), name='api_projects'),
    path('materials', api.MaterialListAPIView.as_view(), name='api_materials'),
]