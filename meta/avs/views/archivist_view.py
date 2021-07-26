from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from avs.models import Arkivar


@login_required(login_url='login_view')
def archivist_view(request, ark):

    arkivar = Arkivar.objects.filter(pk=ark).first()

    return render(request, 'avs/archivist.html', {'arkivar': arkivar})
