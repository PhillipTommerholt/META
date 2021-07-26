from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from avs.models import Av, Leverandor, Medie, Maskine


@login_required(login_url='login_view')
def av_create(request):
    if request.method == 'POST':
        avid = request.POST['avid'] if 'avid' in request.POST else None
        avid = avid.strip()

        try:
            avid = int(avid)
        except ValueError:
            pass

        if isinstance(avid, int) and avid != 0 and len(request.POST['avid']) == 5:

            last_av = Av.objects.filter(avid=avid).order_by('version').last()
            if last_av:
                version = last_av.version
            else:
                version = 0
            version += 1

            if version > 1:
                Av.objects.create(
                    avid=avid,
                    version=version,
                    jnr=last_av.jnr,
                    titel=last_av.titel,
                    kategori=last_av.kategori,
                    klassifikation=last_av.klassifikation,
                    land=last_av.land,
                )
            else:
                Av.objects.create(
                    avid=avid,
                    version=version,
                )

            return redirect('/' + str(avid) + '/' + str(version))

    if request.method == 'GET':
        print('GET')
        avid = request.GET['avid'] if 'avid' in request.GET else None
        avid = avid.strip()

        try:
            avid = int(avid)
        except ValueError:
            pass

        if isinstance(avid, int) and avid != 0 and len(request.GET['avid']) == 5:

            last_av = Av.objects.filter(avid=avid).order_by('version').last()
            if last_av:
                version = last_av.version
            else:
                version = 0
            version += 1

            if version > 1:
                av_obj = Av.objects.create(
                    avid=avid,
                    version=version,
                    jnr=last_av.jnr,
                    titel=last_av.titel,
                    kategori=last_av.kategori,
                    klassifikation=last_av.klassifikation,
                    arkivar=last_av.arkivar,
                    storrelse=last_av.storrelse,
                    leverandor=last_av.leverandor,
                    status='Afventer genaflevering',
                    land=last_av.land,
                    public=last_av.public,
                    maskine=last_av.maskine,
                )
                av_obj.medier.add(*last_av.medier.all())
                last_av.medier.clear()
                last_av.maskine = None
                last_av.save()
            else:
                Av.objects.create(
                    avid=avid,
                    version=version,
                )

        return redirect('/' + str(avid) + '/' + str(version))

#    return redirect('tasks_view')
