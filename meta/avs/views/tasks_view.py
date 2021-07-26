from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.models import User

from avs.models import Av


@login_required(login_url='login_view')
def tasks_view(request):

    tester = User.objects.filter(username=request.user).first()
    avs = Av.objects.filter((Q(afsluttet=False) | Q(bliv=True)), tester=tester).order_by('avid', 'version')

    return render(request, 'avs/tasks.html', {'avs': avs})
