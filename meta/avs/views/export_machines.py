from django.http import HttpResponse

import csv

from avs.models import Maskine


def export_machines(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="machines.csv"'
    writer = csv.writer(response)
    machines = Maskine.objects.all().values_list('navn', 'processor', 'bundkort', 'arbejdshukommelse')
    for machine in machines:
        writer.writerow(machine)
    return response
