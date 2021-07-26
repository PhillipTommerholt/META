from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower
from django.db.models import Q

from avs.models import Medie, Av


@login_required(login_url='login_view')
def drives_view(request):

    medie_objects = Medie.objects.all().order_by(Lower('navn'))

    medier = []

    for medie in medie_objects:

        av_objects = Av.objects.filter(~Q(medier=None))
        dea_objects = Av.objects.filter(~Q(dea_medier=None))

        avs = []
        maskine = ''

        for av in av_objects:
            if Av.objects.filter(medier__pk=medie.pk):
                _avs = Av.objects.filter(medier__pk=medie.pk)
                for _av in _avs:
                    if {'avid': _av.avid, 'version': _av.version} not in avs:
                        avs.append({'avid': _av.avid, 'version': _av.version})
                        if _av.maskine:
                            maskine = _av.maskine

        deas = []
        dmaskine = ''

        for dea in dea_objects:
            if Av.objects.filter(dea_medier__pk=medie.pk):
                _deas = Av.objects.filter(dea_medier__pk=medie.pk)
                for _dea in _deas:
                    if {'avid': _av.avid, 'version': _av.version} not in deas:
                        deas.append({'avid': _av.avid, 'version': _av.version})

        medier.append({
            'pk': medie.pk,
            'navn': medie.navn,
            'producent': medie.producent,
            'kapacitet': medie.kapacitet,
            'type': medie.type,
            'avs': avs,
            'deas': deas,
            'maskine': maskine
        })

    return render(request, 'avs/drives.html', {'medier': medier})
