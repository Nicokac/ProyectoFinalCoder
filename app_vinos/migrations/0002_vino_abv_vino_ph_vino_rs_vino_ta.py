# Generated by Django 5.1.1 on 2024-09-28 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vinos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vino',
            name='abv',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Alcohol by Volume (%)'),
        ),
        migrations.AddField(
            model_name='vino',
            name='ph',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=3, verbose_name='pH'),
        ),
        migrations.AddField(
            model_name='vino',
            name='rs',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Residual Sugar (g/L)'),
        ),
        migrations.AddField(
            model_name='vino',
            name='ta',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4, verbose_name='Total Acidity (g/L)'),
        ),
    ]
