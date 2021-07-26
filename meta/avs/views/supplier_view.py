from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from avs.models import Leverandor


@login_required(login_url='login_view')
def supplier_view(request, lev):

    leverandor = Leverandor.objects.filter(pk=lev).first()

    return render(request, 'avs/supplier.html', {'leverandor': leverandor})
