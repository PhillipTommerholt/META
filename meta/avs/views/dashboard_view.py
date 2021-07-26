from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from avs.models import Av


@login_required(login_url='login_view')
def dashboard_view(request):

    statslige = Av.objects.filter(kategori='Stat', status='Klar til test').order_by('prioritering', 'svarfrist')[:100]
    kommunale = Av.objects.filter(kategori='Kommune', status='Klar til test').order_by('prioritering', 'svarfrist')[:100]
    private = Av.objects.filter(kategori='Privat', status='Klar til test').order_by('prioritering', 'svarfrist')[:100]
    klassificerede = Av.objects.filter(kategori='Klassificeret', status='Klar til test').order_by('prioritering', 'svarfrist')[:100]

    statslige_count = len(statslige)
    kommunale_count = len(kommunale)
    private_count = len(private)
    klassificerede_count = len(klassificerede)

    backoffice = Group.objects.get(name='Backoffice').user_set.filter(username=request.user).exists()

    return render(request, 'avs/dashboard.html', {
        'statslige_count': statslige_count,
        'kommunale_count': kommunale_count,
        'private_count': private_count,
        'klassificerede_count': klassificerede_count,
        'statslige': statslige,
        'kommunale': kommunale,
        'private': private,
        'klassificerede': klassificerede,
        'backoffice': backoffice
    })
