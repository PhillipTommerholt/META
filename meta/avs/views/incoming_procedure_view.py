from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

import json

from avs.models import Av, Leverandor, Medie, Maskine, Modtagelse, Arkivar


@login_required(login_url='login_view')
def incoming_procedure_view(request, a, v=0):

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

    if a == '0':
        avid = request.POST['avid'] if 'avid' in request.POST else None
        avid = avid.strip()
        version = 0

        try:
            avid = int(avid)
        except ValueError:
            pass

        if isinstance(avid, int):
            last_av = Av.objects.filter(avid=avid).order_by('version').last()

            if last_av and last_av.status == 'Afventer genaflevering':

                Modtagelse.objects.create(
                    avid=last_av.avid,
                    version=last_av.version,
                    public=True,
                    journalnummer=True,
                    titel=True,
                    arkivar=True,
                    enhed=True,
                    kategori=True,
                    klassifikation=True,
                    leverandor=True,
                    status='Oprettelse'
                )
                last_av.status = 'Modtaget'
                last_av.save()
                return redirect('/modtagelse_procedure/' + str(last_av.avid) + '/' + str(last_av.version))

            else:

                if last_av:
                    version = last_av.version

                version += 1

                if version > 10:
                    Av.objects.create(
                        avid=avid,
                        version=version,
                        jnr=last_av.jnr,
                        titel=last_av.titel,
                        kategori=last_av.kategori,
                        klassifikation=last_av.klassifikation,
                        land=last_av.land,
                        leverandor=last_av.leverandor,
                        arkivar=last_av.arkivar,
                        status='Modtaget'
                    )
                    Modtagelse.objects.create(
                        avid=avid,
                        version=version,
                        public=True,
                        journalnummer=True,
                        titel=True,
                        arkivar=True,
                        enhed=True,
                        kategori=True,
                        klassifikation=True,
                        leverandor=True,
                        status='Oprettelse'
                    )
                else:
                    Av.objects.create(
                        avid=avid,
                        version=version,
                        status='Modtaget'
                    )
                    Modtagelse.objects.create(
                        avid=avid,
                        version=version,
                        status='Oprettelse'
                    )

            return redirect('incoming_procedure_view', avid, version)
        else:
            return redirect('incoming_view')

    if Modtagelse.objects.filter(avid=a, version=v).exists():

        av = Av.objects.filter(avid=a, version=v).first()
        form = Modtagelse.objects.filter(avid=a, version=v).first()

        if av and form:

            maskiner = []
            if av.maskine:
                maskiner.append(av.maskine)
            else:
                maskiner = Maskine.objects.all().order_by('navn')

            ibrugtaget_medier = []
            for medie in av.medier.all():
                ibrugtaget_medier.append({'tag': medie.navn})
            ibrugtaget_medier = json.dumps(ibrugtaget_medier)

            context = {
                'av': av,
                'form': form,
                'kategorier': kategorier,
                'klassifikationer': klassifikationer,
                'lande': lande,
                'leverandorer': leverandorer,
                'ibrugtaget_medier': ibrugtaget_medier,
                'arkivarer': arkivarer,
                'maskiner': maskiner
            }

            path = ''
            if form.status == 'Oprettelse':
                path = 'avs/incoming_' + 'oprettelse' + '.html'
            if form.status == 'Kvittering':
                path = 'avs/incoming_' + 'kvittering' + '.html'
            if form.status == 'Kodeord':
                path = 'avs/incoming_' + 'kodeord' + '.html'
            if form.status == 'Journalisering':
                path = 'avs/incoming_' + 'journalisering' + '.html'
            if form.status == 'Kopiering':
                path = 'avs/incoming_' + 'kopiering' + '.html'

            return render(request, path, context)
        else:
            return redirect('incoming_view')
    else:
        return redirect('incoming_view')
