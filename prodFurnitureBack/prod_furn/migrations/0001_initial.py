# Generated by Django 5.1.3 on 2024-11-07 17:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('contact_info', models.CharField(max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=60, null=True)),
                ('registration_date', models.DateField(default='2024-11-07')),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('quantity', models.IntegerField()),
                ('unit_price', models.FloatField()),
                ('in_stock', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateField(default='2024-11-07')),
                ('status', models.CharField(blank=True, default='На рассмотрении', max_length=15)),
                ('description', models.TextField(blank=True, null=True)),
                ('expected_completion_date', models.DateField(blank=True, null=True)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prod_furn.client')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('specification', models.CharField(max_length=60)),
                ('predicted_cost', models.FloatField()),
                ('completion_deadline', models.DateField()),
                ('status', models.CharField(blank=True, default='В обработке', max_length=15)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prod_furn.order')),
            ],
        ),
        migrations.CreateModel(
            name='ProjectMaterial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_used', models.IntegerField()),
                ('material_id', models.ManyToManyField(to='prod_furn.material')),
                ('project_id', models.ManyToManyField(to='prod_furn.project')),
            ],
        ),
    ]
