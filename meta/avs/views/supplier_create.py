from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Leverandor


@login_required(login_url='login_view')
def supplier_create(request):

    l = Leverandor.objects.create()

    return redirect('supplier_view', l.pk)
