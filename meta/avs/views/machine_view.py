from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from avs.models import Maskine


@login_required(login_url='login_view')
def machine_view(request, lev):

    maskine = Maskine.objects.filter(pk=lev).first()

    return render(request, 'avs/machine.html', {'maskine': maskine})
