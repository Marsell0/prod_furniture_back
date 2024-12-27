# Generated by Django 5.1.3 on 2024-12-27 06:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prod_furn', '0004_alter_project_completion_deadline'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='projectmaterial',
            name='material_id',
        ),
        migrations.RemoveField(
            model_name='projectmaterial',
            name='project_id',
        ),
        migrations.AddField(
            model_name='projectmaterial',
            name='material',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='material_projects', to='prod_furn.material'),
        ),
        migrations.AddField(
            model_name='projectmaterial',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_materials', to='prod_furn.project'),
        ),
    ]
