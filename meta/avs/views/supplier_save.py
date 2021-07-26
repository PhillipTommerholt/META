from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Leverandor


@login_required(login_url='login_view')
def supplier_save(request):

    navn = request.POST['leverandor']
    pk = request.POST['pk']

    if not Leverandor.objects.filter(navn=navn).first():
        l = Leverandor.objects.get(pk=pk)
        l.navn = navn
        l.save()

    return redirect('suppliers_view')
