# Generated by Django 5.1.1 on 2024-09-28 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vinos', '0002_vino_abv_vino_ph_vino_rs_vino_ta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vino',
            name='intensidad',
            field=models.CharField(max_length=100),
        ),
    ]
