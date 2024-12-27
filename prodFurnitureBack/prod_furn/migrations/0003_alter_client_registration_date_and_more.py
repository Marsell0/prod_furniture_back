# Generated by Django 5.1.3 on 2024-12-27 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_furn', '0002_employee_showcasetype_alter_client_registration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='registration_date',
            field=models.DateField(default='2024-12-27'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='registration_date',
            field=models.DateField(default='2024-12-27'),
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(default='2024-12-27'),
        ),
        migrations.AlterField(
            model_name='project',
            name='predicted_cost',
            field=models.FloatField(null=True),
        ),
    ]
