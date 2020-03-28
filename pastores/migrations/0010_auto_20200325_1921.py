# Generated by Django 3.0.4 on 2020-03-25 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pastores', '0009_auto_20200322_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='persona',
            name='baja',
        ),
        migrations.AlterField(
            model_name='persona',
            name='baja_fecha',
            field=models.DateTimeField(blank=True, default=None, null=True, verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='baja_motivo',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Sin Interés'), (2, 'Falleció'), (3, 'Ya no es pastor')], default=0, verbose_name='Motivo'),
        ),
        migrations.AlterField(
            model_name='persona',
            name='paternidad_fecha',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Fecha'),
        ),
    ]