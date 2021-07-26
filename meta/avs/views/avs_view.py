from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import datetime

import io
from django.http import HttpResponse
from django.views.generic import View
import xlsxwriter
from avs.models import Av, Arkivar, Leverandor, Profile, Medie


@login_required(login_url='login_view')
def avs_view(request, nulstil=0):

    _avid = request.GET.get('avid_soeg') if 'avid_soeg' in request.GET and request.GET.get('avid_soeg') != '' else None
    _jnr = request.GET.get('jnr_soeg') if 'jnr_soeg' in request.GET and request.GET.get('jnr_soeg') != '' else None
    _titel = request.GET.get('titel_soeg') if 'titel_soeg' in request.GET and request.GET.get('titel_soeg') != '' else None
    _land = request.GET.getlist('land_soeg') if 'land_soeg' in request.GET else None
    _status = request.GET.getlist('status_soeg') if 'status_soeg' in request.GET else None
    _kategori = request.GET.getlist('kategori_soeg') if 'kategori_soeg' in request.GET else None
    _klassifikation = request.GET.getlist('klassifikation_soeg') if 'klassifikation_soeg' in request.GET else None
    _arkivar = request.GET.getlist('arkivar_soeg') if 'arkivar_soeg' in request.GET else None
    _leverandoer = request.GET.getlist('leverandoer_soeg') if 'leverandoer_soeg' in request.GET else None
    _tester = request.GET.getlist('tester_soeg') if 'tester_soeg' in request.GET else None
    _modtaget_fra = datetime.strptime(request.GET.get('modtaget_fra_soeg'), '%d-%m-%Y').date() if 'modtaget_fra_soeg' in request.GET and request.GET.get('modtaget_fra_soeg') != '' else None
    _modtaget_til = datetime.strptime(request.GET.get('modtaget_til_soeg'), '%d-%m-%Y').date() if 'modtaget_til_soeg' in request.GET and request.GET.get('modtaget_til_soeg') != '' else None
    _adgang_fra = datetime.strptime(request.GET.get('adgang_fra_soeg'), '%d-%m-%Y').date() if 'adgang_fra_soeg' in request.GET and request.GET.get('adgang_fra_soeg') != '' else None
    _adgang_til = datetime.strptime(request.GET.get('adgang_til_soeg'), '%d-%m-%Y').date() if 'adgang_til_soeg' in request.GET and request.GET.get('adgang_til_soeg') != '' else None
    _svarfrist_fra = datetime.strptime(request.GET.get('svarfrist_fra_soeg'), '%d-%m-%Y').date() if 'svarfrist_fra_soeg' in request.GET and request.GET.get('svarfrist_fra_soeg') != '' else None
    _svarfrist_til = datetime.strptime(request.GET.get('svarfrist_til_soeg'), '%d-%m-%Y').date() if 'svarfrist_til_soeg' in request.GET and request.GET.get('svarfrist_til_soeg') != '' else None
    _svar_fra = datetime.strptime(request.GET.get('svar_fra_soeg'), '%d-%m-%Y').date() if 'svar_fra_soeg' in request.GET and request.GET.get('svar_fra_soeg') != '' else None
    _svar_til = datetime.strptime(request.GET.get('svar_til_soeg'), '%d-%m-%Y').date() if 'svar_til_soeg' in request.GET and request.GET.get('svar_til_soeg') != '' else None

    _sortering_avid = True if request.GET.get('sortering') == 'sortering_avid' else False
    _sortering_status = True if request.GET.get('sortering') == 'sortering_status' else False
    _sortering_adgang = True if request.GET.get('sortering') == 'sortering_adgang' else False
    _sortering_svarfrist = True if request.GET.get('sortering') == 'sortering_svarfrist' else False
    _sortering_faldende = True if request.GET.get('sortering_faldende') != None else False

    _enkelte_versioner = True if request.GET.get('enkelte_versioner') != None else False

    _bookmark = True if 'bookmark' in request.GET else False

    _lande = []
    for land in list(Av._meta.get_field('land').choices):
        _lande.append(land[1])

    _statusser = []
    for status in list(Av._meta.get_field('status').choices):
        _statusser.append(status[1])

    _kategorier = []
    for kategori in list(Av._meta.get_field('kategori').choices):
        _kategorier.append(kategori[1])

    _klassifikationer = []
    for klassifikation in list(Av._meta.get_field('klassifikation').choices):
        _klassifikationer.append(klassifikation[1])

    _arkivarer = []
    for arkivar in Arkivar.objects.all().order_by('navn'):
        _arkivarer.append(arkivar.navn)

    _leverandoerer = []
    for leverandor in Leverandor.objects.all().order_by('navn'):
        _leverandoerer.append(leverandor.navn)

    _testere = []
    for tester in Profile.objects.all():
        if tester.initialer:
            _testere.append(tester.initialer)

    _resultat = list()
    _sorted_resultat = list()
    _arkiveringsversioner = dict()

    if nulstil == 0:

        _avs_objs = Av.objects.all().order_by('avid', 'version')

        if _enkelte_versioner:
            pass

        if _avid:
            _avs_objs = _avs_objs.filter(avid__icontains=_avid)
        if _jnr:
            _avs_objs = _avs_objs.filter(jnr__icontains=_jnr)
        if _titel:
            _avs_objs = _avs_objs.filter(titel__icontains=_titel)
        if _land:
            _avs_objs = _avs_objs.filter(qtq([Q(land=value) for value in _land]))
        if _status:
            _avs_objs = _avs_objs.filter(qtq([Q(status=value) for value in _status]))
        if _kategori:
            _avs_objs = _avs_objs.filter(qtq([Q(kategori=value) for value in _kategori]))
        if _klassifikation:
            _avs_objs = _avs_objs.filter(qtq([Q(klassifikation=value) for value in _klassifikation]))
        if _arkivar:
            _avs_objs = _avs_objs.filter(qtq([Q(arkivar=Arkivar.objects.get(navn=value)) for value in _arkivar]))
        if _leverandoer:
            _avs_objs = _avs_objs.filter(qtq([Q(leverandor=Leverandor.objects.get(navn=value)) for value in _leverandoer]))
        if _tester:
            _avs_objs = _avs_objs.filter(qtq([Q(tester=value) for value in [Profile.objects.get(initialer=value).user for value in _tester]]))

        if _modtaget_fra and not _modtaget_til:
            _avs_objs = _avs_objs.filter(modtaget__gte=_modtaget_fra, modtaget__lte=datetime.now())
        if not _modtaget_fra and _modtaget_til:
            _avs_objs = _avs_objs.filter(modtaget__gte=datetime.strptime('01-01-1970', '%d-%m-%Y').date(), modtaget__lte=_modtaget_til)
        if _modtaget_fra and _modtaget_til:
            _avs_objs = _avs_objs.filter(modtaget__gte=_modtaget_fra, modtaget__lte=_modtaget_til)

        if _adgang_fra and not _adgang_til:
            _avs_objs = _avs_objs.filter(kodeord__gte=_adgang_fra, kodeord__lte=datetime.now())
        if not _adgang_fra and _adgang_til:
            _avs_objs = _avs_objs.filter(kodeord__gte=datetime.strptime('01-01-1970', '%d-%m-%Y').date(), kodeord__lte=_adgang_til)
        if _adgang_fra and _adgang_til:
            _avs_objs = _avs_objs.filter(kodeord__gte=_adgang_fra, kodeord__lte=_adgang_til)

        if _svarfrist_fra and not _svarfrist_til:
            _avs_objs = _avs_objs.filter(svarfrist__gte=_svarfrist_fra, svarfrist__lte=datetime.now())
        if not _svarfrist_fra and _svarfrist_til:
            _avs_objs = _avs_objs.filter(svarfrist__gte=datetime.strptime('01-01-1970', '%d-%m-%Y').date(), svarfrist__lte=_svarfrist_til)
        if _svarfrist_fra and _svarfrist_til:
            _avs_objs = _avs_objs.filter(svarfrist__gte=_svarfrist_fra, svarfrist__lte=_svarfrist_til)

        if _svar_fra and not _svar_til:
            _avs_objs = _avs_objs.filter(svar__gte=_svar_fra, svar__lte=datetime.now())
        if not _svar_fra and _svar_til:
            _avs_objs = _avs_objs.filter(svar__gte=datetime.strptime('01-01-1970', '%d-%m-%Y').date(), svar__lte=_svar_til)
        if _svar_fra and _svar_til:
            _avs_objs = _avs_objs.filter(svar__gte=_svar_fra, svar__lte=_svar_til)

        for _av_obj in _avs_objs:

            _tester_obj = Profile.objects.filter(user=_av_obj.tester).first()

            # if len(_av_obj.medier.all()) > 0:
            #     _medie = _av_obj.medier.all()[0]
            # else:
            #     _medie = None

            _resultat.append({
                "avid": _av_obj.avid,
                "version": _av_obj.version,
                "jnr": _av_obj.jnr,
                "titel": _av_obj.titel,
                "land": _av_obj.land,
                "status": _av_obj.status,
                "kategori": _av_obj.kategori,
                "klassifikation": _av_obj.klassifikation,
                "stoerrelse": _av_obj.storrelse,
                "arkivar": _av_obj.arkivar.navn if _av_obj.arkivar else '',
                "leverandoer": _av_obj.leverandor.navn if _av_obj.leverandor else '',
                "tester": _tester_obj.initialer if _tester_obj else '',
                "modtaget": '{:%d-%m-%Y}'.format(_av_obj.modtaget) if _av_obj.modtaget != None else '',
                "adgang": '{:%d-%m-%Y}'.format(_av_obj.kodeord) if _av_obj.kodeord != None else '',
                "svarfrist": '{:%d-%m-%Y}'.format(_av_obj.svarfrist) if _av_obj.svarfrist != None else '',
                "svar": '{:%d-%m-%Y}'.format(_av_obj.svar) if _av_obj.svar != None else '',
                # "medie": _medie,
            })

    if _sortering_avid:
        if _sortering_faldende:
            _sorted_resultat = sorted(_resultat, key=lambda i: (i['avid'], i['version']), reverse=True)
        else:
            _sorted_resultat = sorted(_resultat, key=lambda i: (i['avid'], i['version']))
    elif _sortering_status:
        if _sortering_faldende:
            _sorted_resultat = sorted(_resultat, key=lambda i: (i['status'], i['avid'], i['version']), reverse=True)
        else:
            _sorted_resultat = sorted(_resultat, key=lambda i: (i['status'], i['avid'], i['version']))
    elif _sortering_adgang:
        if _sortering_faldende:
            _sorted_resultat = sorted(_resultat, key=lambda i: (notnonedate(i['adgang']), i['avid'], i['version']), reverse=True)
        else:
            _sorted_resultat = sorted(_resultat, key=lambda i: (notnonedate(i['adgang']), i['avid'], i['version']))
    elif _sortering_svarfrist:
        if _sortering_faldende:
            _sorted_resultat = sorted(_resultat, key=lambda i: (notnonedate(i['svarfrist']), i['avid'], i['version']), reverse=True)
        else:
            _sorted_resultat = sorted(_resultat, key=lambda i: (notnonedate(i['svarfrist']), i['avid'], i['version']))
    else:
        _sorted_resultat = _resultat

    _samlet_stoerrrelse = 0
    for r in _sorted_resultat:
        try:
            size = float(r['stoerrelse'].replace(',', '.'))
        except ValueError:
            size = 0
        _samlet_stoerrrelse += size
    _temp_str = f"{int(_samlet_stoerrrelse):,}"
    _samlet_stoerrrelse = _temp_str.replace(',', '.')

    if _enkelte_versioner:
        for sr in _sorted_resultat:
            if not sr['avid'] in _arkiveringsversioner:
                _arkiveringsversioner[sr['avid']] = sr['version']
            else:
                if _arkiveringsversioner[sr['avid']] < sr['version']:
                    _arkiveringsversioner[sr['avid']] = sr['version']

        _tmp_resultat = _sorted_resultat.copy()

        for sr in _tmp_resultat:
            if sr['avid'] in _arkiveringsversioner:
                if not sr['version'] == _arkiveringsversioner[sr['avid']]:
                    idx = _sorted_resultat.index(sr)
                    _sorted_resultat.pop(idx)

    xls = request.get_full_path() + '&xls='
    book = request.get_full_path() + '&bookmark='

    if 'xls' in request.GET:
        output = io.BytesIO()
        workbook = xlsxwriter.Workbook(output)
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        date_format = workbook.add_format({'num_format': 'dd-mm-yyyy'})

        titler = ["avid", "version", "jnr", "titel", "land", "status", "kategori", "klassifikation", "arkivar", "leverandør", "tester", "modtaget", "adgang", "svarfrist", "svar", "størrelse"]

        i = 0
        for titel in titler:
            worksheet.write(0, i, titel, bold)
            i += 1

        i = 1
        for sr in _sorted_resultat:
            worksheet.write(i, 0, sr['avid'])
            worksheet.write(i, 1, sr['version'])
            worksheet.write(i, 2, sr['jnr'])
            worksheet.write(i, 3, sr['titel'])
            worksheet.write(i, 4, sr['land'])
            worksheet.write(i, 5, sr['status'])
            worksheet.write(i, 6, sr['kategori'])
            worksheet.write(i, 7, sr['klassifikation'])
            worksheet.write(i, 8, sr['arkivar'])
            worksheet.write(i, 9, sr['leverandoer'])
            worksheet.write(i, 10, sr['tester'])
            if sr['modtaget']:
                worksheet.write_datetime(i, 11, datetime.strptime(sr['modtaget'], '%d-%m-%Y').date(), date_format)
            if sr['adgang']:
                worksheet.write_datetime(i, 12, datetime.strptime(sr['adgang'], '%d-%m-%Y').date(), date_format)
            if sr['svarfrist']:
                worksheet.write_datetime(i, 13, datetime.strptime(sr['svarfrist'], '%d-%m-%Y').date(), date_format)
            if sr['svar']:
                worksheet.write_datetime(i, 14, datetime.strptime(sr['svar'], '%d-%m-%Y').date(), date_format)

            worksheet.write(i, 15, sr['stoerrelse'])
            i += 1

        worksheet.freeze_panes(1, 0)
        workbook.close()
        output.seek(0)
        dt_string = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        filename = 'meta ' + dt_string + '.xlsx'
        response = HttpResponse(
            output,
            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        response['Content-Disposition'] = 'attachment; filename=%s' % filename

        return response

    return render(request, 'avs/avs.html', {
        "avid": _avid,
        "jnr": _jnr,
        "titel": _titel,
        "land": _land,
        "status": _status,
        "kategori": _kategori,
        "klassifikation": _klassifikation,
        "arkivar": _arkivar,
        "leverandoer": _leverandoer,
        "tester": _tester,
        "modtaget_fra": _modtaget_fra,
        "modtaget_til": _modtaget_til,
        "adgang_fra": _adgang_fra,
        "adgang_til": _adgang_til,
        "svarfrist_fra": _svarfrist_fra,
        "svarfrist_til": _svarfrist_til,
        "svar_fra": _svar_fra,
        "svar_til": _svar_til,
        "enkelte_versioner": _enkelte_versioner,
        "nulstil": nulstil,
        "bookmark": _bookmark,
        "resultat": _sorted_resultat,
        "lande": _lande,
        "statusser": _statusser,
        "kategorier": _kategorier,
        "klassifikationer": _klassifikationer,
        "arkivarer": _arkivarer,
        "leverandoerer": _leverandoerer,
        "testere": sorted(_testere),
        "sortering_avid": _sortering_avid,
        "sortering_status": _sortering_status,
        "sortering_adgang": _sortering_adgang,
        "sortering_svarfrist": _sortering_svarfrist,
        "sortering_faldende": _sortering_faldende,
        "resultat": _sorted_resultat,
        "samlet_stoerrrelse": _samlet_stoerrrelse,
        "xls": xls,
        "book": book,
    })


def qtq(queries):
    query = queries.pop()
    for item in queries:
        query |= item
    return query


def notnonedate(date):
    if date:
        return datetime.strptime(date, '%d-%m-%Y').date()
    else:
        return datetime.strptime('01-01-1970', '%d-%m-%Y').date()
