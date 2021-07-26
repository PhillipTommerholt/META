from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Maskine


@login_required(login_url='login_view')
def machine_create(request):

    m = Maskine.objects.create()

    return redirect('machine_view', m.pk)
