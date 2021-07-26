from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Maskine


@login_required(login_url='login_view')
def machine_delete(request, pk):

    m = Maskine.objects.get(pk=pk)

    m.delete()

    return redirect('machines_view')
