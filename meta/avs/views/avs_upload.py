import io
import csv
from datetime import datetime, date

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from avs.models import Av, Leverandor, Medie, Maskine, Profile


@login_required(login_url='login_view')
def avs_upload(request):
    if request.method == 'POST':

        Av.objects.all().delete()
        Leverandor.objects.all().delete()

        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        next(io_string)

        for column in csv.reader(io_string, delimiter=','):

            avid = None
            version = None
            jnr = None
            titel = None
            kategori = None
            klassifikation = None
            land = None
            leverandor = None
            storrelse = None
            modtaget = None
            kodeord = None
            svarfrist = None
            svar = None
            status = None
            tester = None
            afsluttet = None

            if column[7] != '' and not Leverandor.objects.filter(navn=column[7]):
                Leverandor.objects.create(navn=column[7])

            if column[2] != '' and column[6] != '':
                avid = column[2]
                version = column[6]
                jnr = column[0]
                titel = column[1]
                storrelse = column[12]
                status = column[18]
                kategori = column[5]
                klassifikation = 'Ingen'
                land = 'Danmark'

                if column[3] != '':
                    modtaget = datetime.strptime(column[3], '%d/%m/%Y').strftime('%Y-%m-%d')

                if column[4] != '':
                    kodeord = datetime.strptime(column[4], '%d/%m/%Y').strftime('%Y-%m-%d')

                if column[11] != '':
                    svarfrist = datetime.strptime(column[11], '%d/%m/%Y').strftime('%Y-%m-%d')

                if column[19] != '':
                    svar = datetime.strptime(column[19], '%d/%m/%Y').strftime('%Y-%m-%d')

                leverandor = Leverandor.objects.get(navn=column[7])

                tester = None
                if column[17] != '':
                    profile = Profile.objects.filter(initialer=column[17]).first()
                    if profile:
                        tester = User.objects.filter(profile=profile).first()

                afsluttet = False
                if status == 'Tilbagemeldt' or status == 'Godkendt':
                    afsluttet = True

                av = Av.objects.create(avid=avid, version=version)

                av.avid = avid
                av.version = version
                av.jnr = jnr
                av.titel = titel
                av.kategori = kategori
                av.klassifikation = klassifikation
                av.land = land
                av.leverandor = leverandor
                av.storrelse = storrelse
                av.modtaget = modtaget
                av.kodeord = kodeord
                av.svarfrist = svarfrist
                av.svar = svar
                av.status = status
                av.tester = tester
                av.afsluttet = afsluttet

                av.save()

        return render(request, 'avs/avs_upload.html')

    return render(request, 'avs/avs_upload.html')
