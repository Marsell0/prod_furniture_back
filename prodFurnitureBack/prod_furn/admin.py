from django.contrib import admin
from . import models


class ClientAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(models.Client, ClientAdmin)

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)


admin.site.register(models.Order, OrderAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'order_id_id')

admin.site.register(models.Project, ProjectAdmin)


class MaterialAdmin(admin.ModelAdmin):
    list_display = ('name', 'quantity')

admin.site.register(models.Material, MaterialAdmin)


class ProjectMaterialAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.ProjectMaterial, ProjectMaterialAdmin)
# Register your models here.
