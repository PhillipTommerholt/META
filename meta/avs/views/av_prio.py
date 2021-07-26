from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

from avs.models import Av


@login_required(login_url='login_view')
def av_prio(request, avid, version, direction):

    av_active = Av.objects.get(avid=avid, version=version)
    avs = Av.objects.filter(kategori=av_active.kategori).exclude(prioritering=0).order_by('prioritering')
    last_prio_av = Av.objects.filter(kategori=av_active.kategori).exclude(prioritering=0).order_by('prioritering').last()

    if av_active.prioritering != 0:

        if direction == 'up' and len(avs) > 1:

            if av_active.prioritering != -255:
                av_passiv = Av.objects.get(prioritering=av_active.prioritering-1, kategori=av_active.kategori)

                av_active.prioritering = av_active.prioritering - 1
                av_passiv.prioritering = av_passiv.prioritering + 1

                av_active.save()
                av_passiv.save()

        elif direction == 'down':

            if av_active.prioritering != last_prio_av.prioritering:
                av_passiv = Av.objects.get(prioritering=av_active.prioritering+1, kategori=av_active.kategori)

                av_active.prioritering = av_active.prioritering + 1
                av_passiv.prioritering = av_passiv.prioritering - 1

                av_active.save()
                av_passiv.save()
            else:
                av_active.prioritering = 0
                av_active.save()

    else:
        if len(avs) > 0:
            av_active.prioritering = last_prio_av.prioritering + 1
            av_active.save()
        else:
            av_active.prioritering = -255
            av_active.save()

    return redirect('dashboard_view')
