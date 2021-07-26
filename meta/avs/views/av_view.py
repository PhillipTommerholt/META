from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q

import json
import re

from avs.models import Av, Leverandor, Medie, Maskine, Arkivar


@login_required(login_url='login_view')
def av_view(request, avid, version=1):

    if Av.objects.filter(avid=avid, version=version).exists():

        av = Av.objects.get(avid=avid, version=version)

        kategorier = []
        for kategori in list(Av._meta.get_field('kategori').choices):
            kategorier.append(kategori[1])

        klassifikationer = []
        for klassifikation in list(Av._meta.get_field('klassifikation').choices):
            klassifikationer.append(klassifikation[1])

        lande = []
        for land in list(Av._meta.get_field('land').choices):
            lande.append(land[1])

        leverandorer = Leverandor.objects.all().order_by('navn')
        arkivarer = Arkivar.objects.all().order_by('navn')

        maskiner = []
        if av.maskine:
            maskiner.append({'tag': av.maskine.navn})
        maskiner = json.dumps(maskiner)

        ibrugtaget_medier = []
        for medie in av.medier.all():
            ibrugtaget_medier.append({'tag': medie.navn})
        ibrugtaget_medier = json.dumps(ibrugtaget_medier)

        dea_medier = []
        for dmedie in av.dea_medier.all():
            dea_medier.append({'tag': dmedie.navn})
        dea_medier = json.dumps(dea_medier)

        statusser = []
        for status in list(Av._meta.get_field('status').choices):
            statusser.append(status[1])

        testere = []
        aktiv = True
        if av.tester:
            aktiv = True if av.tester.profile.aktiv else False

            if aktiv:
                for tester in User.objects.all().order_by('first_name', 'last_name'):
                    if tester.profile.aktiv:
                        full_name = ''
                        full_name += tester.first_name
                        if tester.profile.mellemnavn != None:
                            full_name += ' '
                            full_name += tester.profile.mellemnavn
                        full_name += ' '
                        full_name += tester.last_name
                        testere.append([tester, full_name])
            else:
                aktiv = False
                full_name = ''
                full_name += av.tester.first_name
                if av.tester.profile.mellemnavn != None:
                    full_name += ' '
                    full_name += av.tester.profile.mellemnavn
                full_name += ' '
                full_name += av.tester.last_name
                testere.append([av.tester, full_name])
        else:
            for tester in User.objects.all().order_by('first_name', 'last_name'):
                if tester.profile.aktiv:
                    full_name = ''
                    full_name += tester.first_name
                    if tester.profile.mellemnavn != None:
                        full_name += ' '
                        full_name += tester.profile.mellemnavn
                    full_name += ' '
                    full_name += tester.last_name
                    testere.append([tester, full_name])

        andre_vers = []

        andre_avs = Av.objects.filter(avid=avid).order_by('version')

        for andre_av in andre_avs:
            andre_vers.append(andre_av.version)

        if 'https' in av.public:
            publicknap = re.search("(https:).*", av.public).group()
        else:
            publicknap = None

        return render(request, 'avs/av.html', {
            'av': av,
            'kategorier': kategorier,
            'klassifikationer': klassifikationer,
            'lande': lande,
            'leverandorer': leverandorer,
            'ibrugtaget_medier': ibrugtaget_medier,
            'dea_medier': dea_medier,
            'maskiner': maskiner,
            'arkivarer': arkivarer,
            'statusser': statusser,
            'testere': testere,
            'aktiv': aktiv,
            'andre_vers': andre_vers,
            'publicknap': publicknap,

        })

    return redirect('avs_view')
