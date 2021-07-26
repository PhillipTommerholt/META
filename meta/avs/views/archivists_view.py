from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from avs.models import Arkivar


@login_required(login_url='login_view')
def archivists_view(request):

    arkivarer = Arkivar.objects.all().order_by(Lower('navn'))

    return render(request, 'avs/archivists.html', {'arkivarer': arkivarer})
