from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Medie


@login_required(login_url='login_view')
def drive_save(request):

    pk = request.POST['pk']
    navn = request.POST['navn']
    producent = request.POST['producent']
    kapacitet = request.POST['kapacitet']
    type = request.POST['type']

    m = Medie.objects.get(pk=pk)
    m.navn = navn
    m.producent = producent
    m.kapacitet = kapacitet
    m.type = type
    m.save()

    return redirect('drives_view')
