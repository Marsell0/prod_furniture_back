from django.urls import path
from . import api

urlpatterns = [
    path('clients/', api.ClientsAPIList.as_view(), name='get_all_clients'),
    path('clients/<int:client_id>', api.ClientsAPIList.as_view(), name='get_client_by_id'),
    path('orders/', api.OrderListView.as_view(), name='order-list'),
    path('orders/<int:pk>/', api.OrderDetailView.as_view(), name='order-detail'),   
    path('projects', api.ProjectListAPIView.as_view(), name='api_projects'),
    path('materials/', api.MaterialListView.as_view(), name='material-list'),
    path('materials/<int:pk>/', api.MaterialDetailView.as_view(), name='material-detail'), 
]