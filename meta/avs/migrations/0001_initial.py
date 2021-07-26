# Generated by Django 3.0.5 on 2020-04-20 09:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Helligdag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dag', models.DateField(unique=True, verbose_name='dag')),
            ],
            options={
                'verbose_name_plural': 'Helligdage',
            },
        ),
        migrations.CreateModel(
            name='Leverandor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Leverandører',
            },
        ),
        migrations.CreateModel(
            name='Maskine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=255)),
                ('processor', models.CharField(default='', max_length=255)),
                ('bundkort', models.CharField(default='', max_length=255)),
                ('arbejdshukommelse', models.IntegerField(default=0, verbose_name='Arbejdshukommelse i GB')),
            ],
            options={
                'verbose_name_plural': 'Maskiner',
            },
        ),
        migrations.CreateModel(
            name='Medie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(default='', max_length=255)),
                ('producent', models.CharField(default='', max_length=255)),
                ('kapacitet', models.IntegerField(default=0, verbose_name='Kapacitet i GB')),
                ('type', models.CharField(choices=[('Solid State Drive', 'Solid State Drive'), ('USB Stick', 'USB Stick'), ('Hard Drive 3.5', 'Hard Drive 3.5'), ('Hard Drive 2.5', 'Hard Drive 2.5')], max_length=255)),
            ],
            options={
                'verbose_name_plural': 'Medier',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mellemnavn', models.CharField(blank=True, max_length=255, null=True, verbose_name='Mellemnavn')),
                ('initialer', models.CharField(blank=True, max_length=3, null=True, verbose_name='Initialer')),
                ('aktiv', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('modtagelse', models.BooleanField(default=False, verbose_name='Modtagelse')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiler',
            },
        ),
        migrations.CreateModel(
            name='Av',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avid', models.CharField(max_length=255)),
                ('version', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)], default=1)),
                ('jnr', models.CharField(blank=True, max_length=255)),
                ('titel', models.CharField(blank=True, max_length=255)),
                ('kategori', models.CharField(blank=True, choices=[('Stat', 'Stat'), ('Kommune', 'Kommune'), ('Privat', 'Privat'), ('Klassificeret', 'Klassificeret')], max_length=255, null=True)),
                ('klassifikation', models.CharField(choices=[('Ingen', 'Ingen'), ('Til tjenestebrug', 'Til tjenestebrug'), ('Andet', 'Andet')], default='in', max_length=255)),
                ('land', models.CharField(choices=[('Danmark', 'Danmark'), ('Grønland', 'Grønland')], default='dk', max_length=255)),
                ('storrelse', models.CharField(blank=True, max_length=255)),
                ('modtaget', models.DateField(blank=True, null=True)),
                ('kodeord', models.DateField(blank=True, null=True)),
                ('svarfrist', models.DateField(blank=True, null=True)),
                ('svar', models.DateField(blank=True, null=True)),
                ('status', models.CharField(blank=True, choices=[('Modtaget', 'Modtaget'), ('Kvitteret', 'Kvitteret'), ('Kopieret', 'Kopieret'), ('Afvikler ADA', 'Afvikler ADA'), ('Klar til test', 'Klar til test'), ('Under test', 'Under test'), ('Godkendt af tester', 'Godkendt af tester'), ('Afvikler DE', 'Afvikler DEA'), ('Afleveret til DEA', 'Afleveret til DEA'), ('Parat til godkendelse', 'Parat til godkendelse'), ('Tilbagemeldt', 'Tilbagemeldt'), ('Godkendt', 'Godkendt')], max_length=255, null=True)),
                ('bliv', models.BooleanField(default=False)),
                ('afsluttet', models.BooleanField(default=False)),
                ('leverandor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='avs.Leverandor')),
                ('maskine', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='avs.Maskine')),
                ('medie', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='avs.Medie')),
                ('tester', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Arkiveringsversioner',
            },
        ),
    ]
