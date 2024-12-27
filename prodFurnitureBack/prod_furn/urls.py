from django.urls import path
from . import api

urlpatterns = [
    # path('login/', api.LoginView.as_view(), name='login'),
    # path('logout/', api.LogoutView.as_view(), name='logout'),
    path('clients/', api.ClientListView.as_view(), name='client-list'),
    path('clients/<int:pk>/', api.ClientDetailView.as_view(), name='client-detail'),
    path('clients/add/', api.AddClientView.as_view(), name='add-client'),
    path('clients/<int:client_id>/delete/', api.DeleteClientView.as_view(), name='delete-client'),

    path('orders/', api.OrderListView.as_view(), name='order-list'),
    path('orders/create/', api.CreateOrderView.as_view(), name='create-order'),
    path('orders/<int:order_id>/delete/', api.DeleteOrderView.as_view(), name='delete-order'),
    path('orders/<int:pk>/', api.OrderDetailView.as_view(), name='order-detail'),  
    path('orders/<int:order_id>/create-project/', api.CreateProjectFromOrderView.as_view(), name='create-project-from-order'),

    path('projects/', api.ProjectListView.as_view(), name='project-list'),
    path('projects/<int:pk>/', api.ProjectDetailView.as_view(), name='project-detail'), 
    path('projects/<int:project_id>/add-material/', api.AddMaterialToProjectView.as_view(), name='add-material'),
    path('projects/<int:project_id>/remove-material/<int:material_id>/', api.RemoveMaterialFromProjectView.as_view(), name='remove-material'),
    
    path('materials/', api.MaterialListView.as_view(), name='material-list'),
    path('materials/<int:pk>/', api.MaterialDetailView.as_view(), name='material-detail'),  
]