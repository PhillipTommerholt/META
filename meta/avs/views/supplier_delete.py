from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from avs.models import Leverandor


@login_required(login_url='login_view')
def supplier_delete(request, pk):

    l = Leverandor.objects.get(pk=pk)

    l.delete()

    return redirect('suppliers_view')
