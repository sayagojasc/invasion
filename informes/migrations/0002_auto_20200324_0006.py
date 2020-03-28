# Generated by Django 3.0.4 on 2020-03-24 00:06

from django.db import migrations, models
import informes.models


class Migration(migrations.Migration):

    dependencies = [
        ('informes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comando',
            name='periodo',
            field=models.IntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021')], default=informes.models.current_year),
        ),
        migrations.AlterField(
            model_name='convencion',
            name='periodo',
            field=models.IntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021')], default=informes.models.current_year),
        ),
        migrations.AlterField(
            model_name='entrenamiento',
            name='periodo',
            field=models.IntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021')], default=informes.models.current_year),
        ),
        migrations.AlterField(
            model_name='escuelasobrenatural',
            name='periodo',
            field=models.IntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021')], default=informes.models.current_year),
        ),
        migrations.AlterField(
            model_name='invasion',
            name='periodo',
            field=models.IntegerField(choices=[(2015, '2015'), (2016, '2016'), (2017, '2017'), (2018, '2018'), (2019, '2019'), (2020, '2020'), (2021, '2021')], default=informes.models.current_year),
        ),
    ]
