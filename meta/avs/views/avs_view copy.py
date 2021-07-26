from django.shortcuts import render
from django.urls import resolve
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.forms.models import model_to_dict
import xlwt
import datetime as dt
from avs.models import Av, Arkivar, Leverandor, Profile


@login_required(login_url='login_view')
def avs_view(request):

    avs = Av.objects.all().order_by('svarfrist', 'avid', 'version')

    lande = []
    for l in list(Av._meta.get_field('land').choices):
        lande.append(l[1])

    kategorier = []
    for k in list(Av._meta.get_field('kategori').choices):
        kategorier.append(k[1])

    klassifikationer = []
    for kl in list(Av._meta.get_field('klassifikation').choices):
        klassifikationer.append(kl[1])

    leverandorer = []
    for le in list(Leverandor.objects.all().order_by('navn')):
        leverandorer.append(le.navn)

    arkivarer = []
    for a in list(Arkivar.objects.all().order_by('navn')):
        arkivarer.append(a.navn)

    testere = []
    for t in list(User.objects.all().order_by('first_name', 'last_name')):
        if t.profile.initialer:
            testere.append(t.profile.initialer)

    statusser = []
    for s in list(Av._meta.get_field('status').choices):
        statusser.append(s[1])

    bookmark = True if 'bookmark' in request.GET else False
    pagetitle = request.GET['pagetitle'] if 'pagetitle' in request.GET else ''

    titel = request.GET['titel'] if 'titel' in request.GET else ''
    land = request.GET['land'] if 'land' in request.GET else ''
    sidste_version = True if 'sidste_version' in request.GET else False
    kategori = request.GET['kategori'] if 'kategori' in request.GET else ''
    klassifikation = request.GET['klassifikation'] if 'klassifikation' in request.GET else ''
    arkivar = request.GET['arkivar'] if 'arkivar' in request.GET else ''
    leverandor = request.GET['leverandor'] if 'leverandor' in request.GET else ''
    tester = request.GET['tester'] if 'tester' in request.GET else ''
    status = request.GET['status'] if 'status' in request.GET else ''
    modtaget_start = request.GET['modtaget_start'] if 'modtaget_start' in request.GET else ''
    modtaget_slut = request.GET['modtaget_slut'] if 'modtaget_slut' in request.GET else ''
    adgang_start = request.GET['adgang_start'] if 'adgang_start' in request.GET else ''
    adgang_slut = request.GET['adgang_slut'] if 'adgang_slut' in request.GET else ''
    svarfrist_start = request.GET['svarfrist_start'] if 'svarfrist_start' in request.GET else ''
    svarfrist_slut = request.GET['svarfrist_slut'] if 'svarfrist_slut' in request.GET else ''
    svar_start = request.GET['svar_start'] if 'svar_start' in request.GET else ''
    svar_slut = request.GET['svar_slut'] if 'svar_slut' in request.GET else ''

    if 'titel' in request.GET:

        if titel:
            avs = avs.filter(titel__icontains=titel)

        if land:
            avs = avs.filter(land__icontains=land)

        if kategori:
            avs = avs.filter(kategori__icontains=kategori)

        if klassifikation:
            avs = avs.filter(klassifikation__icontains=klassifikation)

        if leverandor:
            l = Leverandor.objects.filter(navn=leverandor).first()
            avs = avs.filter(leverandor__navn__icontains=l.navn)

        if arkivar:
            a = Arkivar.objects.filter(navn=arkivar).first()
            avs = avs.filter(arkivar__navn__icontains=a.navn)

        if status:
            avs = avs.filter(status__icontains=status)

        if modtaget_start and not modtaget_slut:

            start = None
            slut = dt.datetime.now()

            try:
                start = dt.datetime.strptime(modtaget_start, '%d-%m-%Y').date()
            except ValueError as e:
                modtaget_start = ''

            if start and slut:
                avs = avs.filter(modtaget__gte=start, modtaget__lte=slut)

        if not modtaget_start and modtaget_slut:

            start = dt.datetime.strptime('01-01-1970', '%d-%m-%Y').date()
            slut = None

            try:
                slut = dt.datetime.strptime(modtaget_slut, '%d-%m-%Y').date()
            except ValueError as e:
                modtaget_slut = ''

            if start and slut:
                avs = avs.filter(modtaget__gte=start, modtaget__lte=slut)

        if modtaget_start and modtaget_slut:

            start = None
            slut = None

            try:
                start = dt.datetime.strptime(modtaget_start, '%d-%m-%Y').date()
            except ValueError as e:
                modtaget_start = ''

            try:
                slut = dt.datetime.strptime(modtaget_slut, '%d-%m-%Y').date()
            except ValueError:
                modtaget_slut = ''

            if start and slut:
                avs = avs.filter(modtaget__gte=start, modtaget__lte=slut)

        if adgang_start and not adgang_slut:

            start = None
            slut = dt.datetime.now()

            try:
                start = dt.datetime.strptime(adgang_start, '%d-%m-%Y').date()
            except ValueError as e:
                adgang_start = ''

            if start and slut:
                avs = avs.filter(kodeord__gte=start, kodeord__lte=slut)

        if not adgang_start and adgang_slut:

            start = dt.datetime.strptime('01-01-1970', '%d-%m-%Y').date()
            slut = None

            try:
                slut = dt.datetime.strptime(adgang_slut, '%d-%m-%Y').date()
            except ValueError as e:
                adgang_slut = ''

            if start and slut:
                avs = avs.filter(kodeord__gte=start, kodeord__lte=slut)

        if adgang_start and adgang_slut:

            start = None
            slut = None

            try:
                start = dt.datetime.strptime(adgang_start, '%d-%m-%Y').date()
            except ValueError as e:
                adgang_start = ''

            try:
                slut = dt.datetime.strptime(adgang_slut, '%d-%m-%Y').date()
            except ValueError:
                adgang_slut = ''

            if start and slut:
                avs = avs.filter(kodeord__gte=start, kodeord__lte=slut)

        if svarfrist_start and not svarfrist_slut:

            start = None
            slut = dt.datetime.now()

            try:
                start = dt.datetime.strptime(svarfrist_start, '%d-%m-%Y').date()
            except ValueError as e:
                svarfrist_start = ''

            if start and slut:
                avs = avs.filter(svarfrist__gte=start, svarfrist__lte=slut)

        if not svarfrist_start and svarfrist_slut:

            start = dt.datetime.strptime('01-01-1970', '%d-%m-%Y').date()
            slut = None

            try:
                slut = dt.datetime.strptime(svarfrist_slut, '%d-%m-%Y').date()
            except ValueError as e:
                svarfrist_slut = ''

            if start and slut:
                avs = avs.filter(svarfrist__gte=start, svarfrist__lte=slut)

        if svarfrist_start and svarfrist_slut:

            start = None
            slut = None

            try:
                start = dt.datetime.strptime(svarfrist_start, '%d-%m-%Y').date()
            except ValueError as e:
                svarfrist_start = ''

            try:
                slut = dt.datetime.strptime(svarfrist_slut, '%d-%m-%Y').date()
            except ValueError:
                svarfrist_slut = ''

            if start and slut:
                avs = avs.filter(svarfrist__gte=start, svarfrist__lte=slut)

        if svar_start and not svar_slut:

            start = None
            slut = dt.datetime.now()

            try:
                start = dt.datetime.strptime(svar_start, '%d-%m-%Y').date()
            except ValueError as e:
                svar_start = ''

            if start and slut:
                avs = avs.filter(svar__gte=start, svar__lte=slut)

        if not svar_start and svar_slut:

            start = dt.datetime.strptime('01-01-1970', '%d-%m-%Y').date()
            slut = None

            try:
                slut = dt.datetime.strptime(svar_slut, '%d-%m-%Y').date()
            except ValueError as e:
                svar_slut = ''

            if start and slut:
                avs = avs.filter(svar__gte=start, svar__lte=slut)

        if svar_start and svar_slut:

            start = None
            slut = None

            try:
                start = dt.datetime.strptime(svar_start, '%d-%m-%Y').date()
            except ValueError as e:
                frist_start = ''

            try:
                slut = dt.datetime.strptime(svar_slut, '%d-%m-%Y').date()
            except ValueError:
                svar_slut = ''

            if start and slut:
                avs = avs.filter(svar__gte=start, svar__lte=slut)

        xls = request.get_full_path() + '&xls='

        avs = list(avs)

        if sidste_version:
            _avs = []
            for av in avs:
                last_av = Av.objects.filter(avid=av.avid).order_by('version').last()
                if last_av not in _avs:
                    _avs.append(last_av)
            avs = _avs

        if tester:
            _avs = []
            t = Profile.objects.filter(initialer=tester).first()
            for av in avs:
                if av.tester == t.user:
                    _avs.append(av)
            avs = _avs

        count = len(avs)

        total_size = 0
        for av in avs:
            try:
                size = float(av.storrelse.replace(',', '.'))
            except ValueError:
                size = 0

            total_size += size
        total_size = str(round(total_size, 2)).replace('.', ',')

        if 'xls' in request.GET:
            response = HttpResponse(content_type='application/ms-excel')
            response['Content-Disposition'] = 'attachment; filename="avs.xls"'

            wb = xlwt.Workbook(encoding='utf-8')
            ws = wb.add_sheet('avs')

            columns = ['avid', 'version', 'jnr', 'titel', 'kategori', 'klassifikation', 'land', 'leverandor', 'storrelse', 'modtaget', 'kodeord', 'svarfrist', 'svar', 'status', 'arkivar', 'tester', 'antal_arbejdsdage', 'antal_arbejdsdage_med_coronadage']

            row_num = 0
            for col_num in range(len(columns)):
                value = columns[col_num]
                if value == 'kodeord':
                    value = 'adgang'
                if value == 'antal_arbejdsdage':
                    value = 'arbejdsdage'
                if value == 'antal_arbejdsdage_med_coronadage':
                    value = 'arbejdsdage uden hensyn til corona'
                ws.write(row_num, col_num, value)

            row_num = 0
            col_num = 0
            for row in avs:
                _row = model_to_dict(row)
                row_num += 1
                col_num = 0
                for col in columns:
                    value = str(_row[col])

                    if col == 'leverandor':
                        if _row[col] != None:
                            value = Leverandor.objects.filter(id=_row[col]).first().navn

                    if col == 'arkivar':
                        if _row[col] != None:
                            value = Arkivar.objects.filter(id=_row[col]).first().navn

                    if col == 'tester':
                        if _row[col] != None:
                            value = Profile.objects.filter(user_id=_row[col]).first().initialer

                    if col == 'modtaget' or col == 'kodeord' or col == 'svarfrist' or col == 'svar':
                        if _row[col] != None:
                            value = dt.datetime.strptime(str(_row[col]), '%Y-%m-%d').strftime('%d-%m-%Y')

                    if value == 'None':
                        value = ''

                    ws.write(row_num, col_num, value)
                    col_num += 1

            wb.save(response)
            return response

        return render(request, 'avs/avs.html', {
            'avs': avs,
            'titel': titel,
            'land': land,
            'sidste_version': sidste_version,
            'kategori': kategori,
            'klassifikation': klassifikation,
            'arkivar': arkivar,
            'leverandor': leverandor,
            'tester': tester,
            'status': status,
            'modtaget_start': modtaget_start,
            'modtaget_slut': modtaget_slut,
            'adgang_start': adgang_start,
            'adgang_slut': adgang_slut,
            'svarfrist_start': svarfrist_start,
            'svarfrist_slut': svarfrist_slut,
            'svar_start': svar_start,
            'svar_slut': svar_slut,
            'lande': lande,
            'kategorier': kategorier,
            'klassifikationer': klassifikationer,
            'arkivarer': arkivarer,
            'leverandorer': leverandorer,
            'testere': testere,
            'statusser': statusser,
            'start': False,
            'bookmark': bookmark,
            'pagetitle': pagetitle,
            'count': count,
            'total_size': total_size,
            'xls': xls
        })
    else:
        return render(request, 'avs/avs.html', {
            'lande': lande,
            'kategorier': kategorier,
            'klassifikationer': klassifikationer,
            'arkivarer': arkivarer,
            'leverandorer': leverandorer,
            'testere': testere,
            'statusser': statusser,
            'start': True,
            'bookmark': bookmark
        })
