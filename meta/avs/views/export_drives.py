from django.http import HttpResponse

import csv

from avs.models import Medie


def export_drives(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="drives.csv"'
    writer = csv.writer(response)
    drives = Medie.objects.all().values_list('navn', 'producent', 'kapacitet', 'type')
    for drive in drives:
        writer.writerow(drive)
    return response
