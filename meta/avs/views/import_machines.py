from django.shortcuts import render

from avs.models import Maskine

import io
import csv


def import_machines(request):
    if request.method == 'POST':

        Maskine.objects.all().delete()

        csv_file = request.FILES['file']
        data_set = csv_file.read().decode('UTF-8')
        io_string = io.StringIO(data_set)
        # next(io_string)

        for col in csv.reader(io_string, delimiter=','):
            navn = col[0]
            print(navn)
            processor = col[1]
            print(processor)
            bundkort = col[2]
            print(bundkort)
            arbejdshukommelse = col[3]
            print(arbejdshukommelse)

            maskine = Maskine.objects.create()

            maskine.navn = navn
            maskine.processor = processor
            maskine.bundkort = bundkort
            maskine.arbejdshukommelse = arbejdshukommelse

            maskine.save()

        return render(request, 'avs/import_machines.html')

    return render(request, 'avs/import_machines.html')
