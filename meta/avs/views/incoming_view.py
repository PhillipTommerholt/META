from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from avs.models import Av, Modtagelse


@login_required(login_url='login_view')
def incoming_view(request):

    modtagelser = Modtagelse.objects.all()

    avs = []
    for modtagelse in modtagelser:
        av = Av.objects.filter(avid=modtagelse.avid, version=int(modtagelse.version)).first()
        avs.append({
            'av': av,
            'form': modtagelse
        })

    return render(request, 'avs/incoming.html', {
        'avs': avs
    })
