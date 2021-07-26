from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from avs.models import Maskine, Av


@login_required(login_url='login_view')
def machines_view(request):

    maskine_objects = Maskine.objects.all().order_by(Lower('navn'))
    av_objects = Av.objects.all()

    maskiner = []
    for maskine in maskine_objects:

        avs = []
        medier = []
        for av in av_objects:
            if av.maskine:
                if av.maskine == maskine:
                    avs.append({'avid': av.avid, 'version': av.version})

                    _av = Av.objects.filter(avid=av.avid, version=av.version).first()
                    _av_medier = _av.medier.all()
                    for _av_medie in _av_medier:
                        if _av_medie.navn not in medier:
                            medier.append(_av_medie.navn)

        maskiner.append({
            'pk': maskine.pk,
            'navn': maskine.navn,
            'processor': maskine.processor,
            'bundkort': maskine.bundkort,
            'arbejdshukommelse': maskine.arbejdshukommelse,
            'ibrug': maskine.ibrug,
            'avs': avs,
            'medier': medier
        })

    return render(request, 'avs/machines.html', {'maskiner': maskiner})
