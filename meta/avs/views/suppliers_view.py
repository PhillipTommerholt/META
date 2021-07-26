from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models.functions import Lower

from avs.models import Leverandor


@login_required(login_url='login_view')
def suppliers_view(request):

    leverandorer = Leverandor.objects.all().order_by(Lower('navn'))

    return render(request, 'avs/suppliers.html', {'leverandorer': leverandorer})
