# Generated by Django 3.0.4 on 2020-03-21 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastores', '0006_auto_20200321_2017'),
    ]

    operations = [
        migrations.AddField(
            model_name='persona',
            name='paternidad_fecha',
            field=models.DateField(default=None, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='baja_fecha',
            field=models.DateTimeField(default=None, null=True),
        ),
    ]
