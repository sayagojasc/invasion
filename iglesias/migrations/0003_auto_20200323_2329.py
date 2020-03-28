# Generated by Django 3.0.4 on 2020-03-23 23:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pastores', '0009_auto_20200322_0002'),
        ('iglesias', '0002_auto_20200322_0002'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='iglesia',
            options={'verbose_name': 'Iglesia', 'verbose_name_plural': 'Iglesias'},
        ),
        migrations.AlterField(
            model_name='iglesia',
            name='pastor',
            field=models.ForeignKey(limit_choices_to={'distincion': 1, 'esposa': None}, null=True, on_delete=django.db.models.deletion.PROTECT, to='pastores.Persona'),
        ),
    ]