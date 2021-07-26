from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from avs.models import Arkivar


@login_required(login_url='login_view')
def archivist_save(request):

    navn = request.POST['arkivar']
    pk = request.POST['pk']

    if not Arkivar.objects.filter(navn=navn).first():
        a = Arkivar.objects.get(pk=pk)
        a.navn = navn
        a.save()

    return redirect('archivists_view')
