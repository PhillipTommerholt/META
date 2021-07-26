from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from avs.models import Arkivar


@login_required(login_url='login_view')
def archivist_create(request):

    a = Arkivar.objects.create()

    return redirect('archivist_view', a.pk)
