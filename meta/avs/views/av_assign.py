from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from avs.models import Av


@login_required(login_url='login_view')
def av_assign(request, avid, version=1):

    tester = User.objects.get(username=request.user)
    av = Av.objects.get(avid=avid, version=version)

    av.tester = tester
    av.status = 'Under test'
    av.prioritering = 0
    av.save()

    avs = Av.objects.filter(kategori=av.kategori).exclude(prioritering=0).order_by('prioritering')
    i = -255
    for a in avs:
        a.prioritering = i
        a.save()
        i += 1

    return redirect('/' + str(avid) + '/' + str(version))
