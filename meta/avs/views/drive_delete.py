from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Medie


@login_required(login_url='login_view')
def drive_delete(request, pk):

    m = Medie.objects.get(pk=pk)

    m.delete()

    return redirect('drives_view')
