# Generated by Django 3.0.7 on 2020-07-02 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avs', '0036_helligdag_corona'),
    ]

    operations = [
        migrations.AddField(
            model_name='av',
            name='antal_arbejdsdage_med_coronadage',
            field=models.IntegerField(default=0),
        ),
    ]
