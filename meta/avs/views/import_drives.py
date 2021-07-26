from django.shortcuts import render

from avs.models import Medie

import io
import csv


def import_drives(request):
    if request.method == 'POST':

        Medie.objects.all().delete()

        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        # next(io_string)

        for col in csv.reader(io_string, delimiter=','):
            navn = col[0]
            producent = col[1]
            kapacitet = col[2]
            type = col[3]

            drive = Medie.objects.create()

            drive.navn = navn
            drive.producent = producent
            drive.kapacitet = kapacitet
            drive.type = type

            drive.save()

        return render(request, 'avs/import_drives.html')

    return render(request, 'avs/import_drives.html')
