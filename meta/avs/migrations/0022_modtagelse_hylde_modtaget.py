# Generated by Django 3.0.5 on 2020-05-04 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avs', '0021_maskine_ibrug'),
    ]

    operations = [
        migrations.AddField(
            model_name='modtagelse',
            name='hylde_modtaget',
            field=models.BooleanField(default=False),
        ),
    ]
