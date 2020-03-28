# Generated by Django 3.0.4 on 2020-03-27 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paises', '0002_auto_20200326_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ciudad',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='ciudad',
            unique_together={('nombre', 'provincia')},
        ),
    ]
