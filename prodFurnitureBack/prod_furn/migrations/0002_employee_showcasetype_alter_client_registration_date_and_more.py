# Generated by Django 5.1.3 on 2024-12-26 09:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_furn', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('login', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30, verbose_name='password')),
                ('is_admin', models.BooleanField(default=False, verbose_name='is_admin')),
                ('registration_date', models.DateField(default='2024-12-26')),
            ],
        ),
        migrations.CreateModel(
            name='ShowcaseType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateField(default='2024-12-26'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default='2024-12-26'),
        ),
        migrations.CreateModel(
            name='Showcase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('photo', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=20)),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='prod_furn.order')),
            ],
        ),
    ]