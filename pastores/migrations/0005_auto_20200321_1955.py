# Generated by Django 3.0.4 on 2020-03-21 19:55

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('pastores', '0004_auto_20200321_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matrimonio',
            name='esposa',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='esposa', related_query_name='esposa', to='pastores.Persona'),
        ),
        migrations.AlterField(
            model_name='matrimonio',
            name='esposo',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='esposo', related_query_name='esposo', to='pastores.Persona'),
        ),
        migrations.CreateModel(
            name='Telefono',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('tipo', models.IntegerField(choices=[(1, 'Móvil'), (2, 'Casa'), (3, 'Trabajo')], default=1)),
                ('whatsapp', models.BooleanField(default=False)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pastores.Persona')),
            ],
        ),
    ]