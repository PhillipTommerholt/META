from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Maskine


@login_required(login_url='login_view')
def machine_save(request):

    pk = request.POST['pk']
    navn = request.POST['navn']
    processor = request.POST['processor']
    bundkort = request.POST['bundkort']
    arbejdshukommelse = request.POST['arbejdshukommelse']

    m = Maskine.objects.get(pk=pk)
    m.navn = navn
    m.processor = processor
    m.bundkort = bundkort
    m.arbejdshukommelse = arbejdshukommelse
    m.save()

    return redirect('machines_view')
