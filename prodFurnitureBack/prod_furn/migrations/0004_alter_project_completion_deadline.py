# Generated by Django 5.1.3 on 2024-12-27 06:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_furn', '0003_alter_client_registration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='completion_deadline',
            field=models.DateField(null=True),
        ),
    ]