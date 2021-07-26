from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from avs.models import Medie


@login_required(login_url='login_view')
def drive_view(request, lev):

    medie = Medie.objects.filter(pk=lev).first()

    typer = []
    for type in list(Medie._meta.get_field('type').choices):
        typer.append(type[1])

    return render(request, 'avs/drive.html', {
        'medie': medie,
        'typer': typer
    })
