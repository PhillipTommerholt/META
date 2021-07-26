from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
import datetime as dt
import json

from avs.models import Av, Leverandor, Medie, Maskine, Helligdag, Profile, Arkivar


@login_required(login_url='login_view')
def av_save(request):
    if request.method == 'POST':

        avid = request.POST['avid'] if 'avid' in request.POST else None

        if '1' in request.POST:
            return redirect('/' + str(avid) + '/' + str(1))

        if '2' in request.POST:
            return redirect('/' + str(avid) + '/' + str(2))

        if '3' in request.POST:
            return redirect('/' + str(avid) + '/' + str(3))

        if '4' in request.POST:
            return redirect('/' + str(avid) + '/' + str(4))

        if '5' in request.POST:
            return redirect('/' + str(avid) + '/' + str(5))

        if '6' in request.POST:
            return redirect('/' + str(avid) + '/' + str(6))

        if '7' in request.POST:
            return redirect('/' + str(avid) + '/' + str(7))

        if '8' in request.POST:
            return redirect('/' + str(avid) + '/' + str(8))

        if '9' in request.POST:
            return redirect('/' + str(avid) + '/' + str(9))

        if '10' in request.POST:
            return redirect('/' + str(avid) + '/' + str(10))

        if '11' in request.POST:
            return redirect('/' + str(avid) + '/' + str(11))

        if '12' in request.POST:
            return redirect('/' + str(avid) + '/' + str(12))

        if '13' in request.POST:
            return redirect('/' + str(avid) + '/' + str(13))

        if '14' in request.POST:
            return redirect('/' + str(avid) + '/' + str(14))

        if '15' in request.POST:
            return redirect('/' + str(avid) + '/' + str(15))

        version = request.POST['version'] if 'version' in request.POST else None
        jnr = request.POST['jnr'] if 'jnr' in request.POST else None
        titel = request.POST['titel'] if 'titel' in request.POST else None
        kategori = request.POST['kategori'] if 'kategori' in request.POST else None
        klassifikation = request.POST['klassifikation'] if 'klassifikation' in request.POST else None
        land = request.POST['land'] if 'land' in request.POST else None
        leverandor = request.POST['leverandor'] if 'leverandor' in request.POST else None
        storrelse = request.POST['storrelse'] if 'storrelse' in request.POST else None
        modtaget = request.POST['modtaget'] if 'modtaget' in request.POST else None
        kodeord = request.POST['kodeord'] if 'kodeord' in request.POST else None
        svarfrist = request.POST['svarfrist'] if 'svarfrist' in request.POST else None
        svar = request.POST['svar'] if 'svar' in request.POST else None
        status = request.POST['status'] if 'status' in request.POST else None
        arkivar = request.POST['arkivar'] if 'arkivar' in request.POST else None
        tester = request.POST['tester'] if 'tester' in request.POST else None
        afsluttet = True if status == 'Tilbagemeldt' or status == 'Godkendt' else False
        prioritering = True if 'prioritering' in request.POST else False
        public = request.POST['public'] if 'public' in request.POST else None

        if not svar and (status == 'Tilbagemeldt' or status == 'Godkendt'):
            svar = dt.date.today()
        elif svar:
            svar = dt.datetime.strptime(svar, '%d.%m.%Y').date()
        else:
            svar = None

        if avid and version:
            av = Av.objects.get(avid=avid, version=version)

            av.jnr = jnr
            av.titel = titel
            av.kategori = kategori
            av.klassifikation = klassifikation
            av.land = land
            av.leverandor = Leverandor.objects.filter(navn=leverandor).first() if leverandor else None
            av.storrelse = storrelse
            av.modtaget = dt.datetime.strptime(modtaget, '%d.%m.%Y').date() if modtaget else None
            av.kodeord = dt.datetime.strptime(kodeord, '%d.%m.%Y').date() if kodeord else None
            av.svarfrist = dt.datetime.strptime(svarfrist, '%d.%m.%Y').date() if svarfrist else None
            av.svar = svar
            av.public = public

            maskine = ''
            _maskiner = json.loads(request.POST['maskine'])
            if len(_maskiner) > 0:
                maskine = _maskiner[0]['tag'].upper()

            if maskine and not av.maskine:
                av.maskine = Maskine.objects.filter(navn=maskine).first()
            elif not maskine and av.maskine:
                av.maskine = None

            medier = []
            _mer = request.POST['av_medier']

            for _m in json.loads(_mer):
                medier.append(_m['tag'].upper())

            av.medier.clear()
            for medie in medier:
                _medie = Medie.objects.filter(navn=medie).first()
                if (_medie):
                    av.medier.add(_medie)

            if av.medier.count() == 0 and av.maskine:
                av.maskine = None

            dea_medier = []
            _deamer = request.POST['dea_medier']

            for _deam in json.loads(_deamer):
                dea_medier.append(_deam['tag'].upper())

            av.dea_medier.clear()
            for dea_medie in dea_medier:
                _deamedie = Medie.objects.filter(navn=dea_medie).first()
                if (_deamedie):
                    av.dea_medier.add(_deamedie)

            bliv = True if 'bliv' in request.POST else False
            bliv = True if bliv and av.maskine else False

            av_status = av.status
            av.status = status
            av.arkivar = Arkivar.objects.filter(navn=arkivar).first() if arkivar else None
            av.tester = User.objects.filter(username=tester).first()
            av.bliv = bliv
            av.afsluttet = afsluttet

            if not av.svarfrist and av.kodeord:
                av.svarfrist = add_days(av.kodeord, 90)

            if Group.objects.get(name='Backoffice').user_set.filter(username=request.user).exists():
                if not prioritering:
                    av.prioritering = 0
                else:
                    last_prio_av = Av.objects.filter(kategori=av.kategori).exclude(prioritering=0).order_by('prioritering').last()

                    if not last_prio_av:
                        av.prioritering = -255
                    else:
                        av.prioritering = last_prio_av.prioritering+1

            av.save()

            avs = Av.objects.filter(kategori=av.kategori).exclude(prioritering=0).order_by('prioritering')
            i = -255
            for a in avs:
                a.prioritering = i
                a.save()
                i += 1

            if status == 'Tilbagemeldt' and av_status != 'Tilbagemeldt':
                return redirect('/av_create/?avid=' + str(avid))

            return redirect('/' + str(avid) + '/' + str(version))

    return redirect('avs_view')


def add_days(start_date, added_days):
    holidays = []

    holiday_objs = Helligdag.objects.all()
    for holiday_obj in holiday_objs:
        holidays.append(holiday_obj.dag)

    days_elapsed = 0
    while days_elapsed < added_days:
        test_date = start_date+dt.timedelta(days=1)
        start_date = test_date
        if test_date in holidays:
            continue
        else:
            days_elapsed += 1

    return start_date
