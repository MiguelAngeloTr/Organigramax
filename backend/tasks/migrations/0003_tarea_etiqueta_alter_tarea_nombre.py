# Generated by Django 5.1 on 2024-09-04 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_tarea_fecha_tarea_fecha_escogida_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tarea',
            name='etiqueta',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='tarea',
            name='nombre',
            field=models.CharField(max_length=200),
        ),
    ]
