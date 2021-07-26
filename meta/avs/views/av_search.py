from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Av, Modtagelse


@login_required(login_url='login_view')
def av_search(request):
    if request.method == 'POST':
        avid = request.POST['avid'] if 'avid' in request.POST else None
        avid = avid.strip()

        if avid:
            av = Av.objects.filter(avid=avid).order_by('version').last()

            if av:
                if Modtagelse.objects.filter(avid=av.avid, version=av.version).exists():
                    return redirect('/modtagelse_procedure/' + str(av.avid) + '/' + str(av.version))
                return redirect('/' + str(av.avid) + '/' + str(av.version))

    return redirect('tasks_view')
