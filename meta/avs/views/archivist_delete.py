from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from avs.models import Arkivar


@login_required(login_url='login_view')
def archivist_delete(request, pk):

    a = Arkivar.objects.get(pk=pk)

    a.delete()

    return redirect('archivists_view')
