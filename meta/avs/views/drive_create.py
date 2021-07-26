from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Medie


@login_required(login_url='login_view')
def drive_create(request):

    m = Medie.objects.create()

    return redirect('drive_view', m.pk)
