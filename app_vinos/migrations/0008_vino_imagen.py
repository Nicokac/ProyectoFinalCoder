# Generated by Django 5.1.1 on 2024-10-12 21:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_vinos', '0007_cata_tipo_de_cata'),
    ]

    operations = [
        migrations.AddField(
            model_name='vino',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='vinos'),
        ),
    ]
