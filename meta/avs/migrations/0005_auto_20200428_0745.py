# Generated by Django 3.0.5 on 2020-04-28 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avs', '0004_remove_modtagelse_slet_kodeord'),
    ]

    operations = [
        migrations.AddField(
            model_name='modtagelse',
            name='epost_emne',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='modtagelse',
            name='find_epost',
            field=models.BooleanField(default=False),
        ),
    ]
