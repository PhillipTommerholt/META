from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
import datetime as dt

from avs.models import Av, Helligdag

holidays = []
coronadays = []


@login_required(login_url='login_view')
def genberegn_svarfrist(request):
    global holidays
    global coronadays

    holiday_objs = Helligdag.objects.all().order_by('dag')
    for holiday_obj in holiday_objs:
        holidays.append(holiday_obj.dag)
        if holiday_obj.corona:
            coronadays.append(holiday_obj.dag)

    if request.method == 'GET':
        # avs = Av.objects.filter(avid=19525)
        avs = Av.objects.all().order_by('kodeord')

        for av in avs:
            if av.kodeord != None:
                av.svarfrist = add_days(av.kodeord, 90)
                #print('\navid:', av.avid, ', adgang:', av.kodeord, ', svarfrist:', add_days(av.kodeord, 90), ', svar:', av.svar)

            if av.kodeord != None and av.svar != None:
                av.antal_arbejdsdage = business_days(av.kodeord, av.svar)
                av.antal_arbejdsdage_med_coronadage = business_with_corona_days(av.kodeord, av.svar)
                #print('arbejdsdage:', business_days(av.kodeord, av.svar), ', arbejdsdage med coronadage:', business_with_corona_days(av.kodeord, av.svar))

            av.save()

        return redirect('avs_view')

    return redirect('avs_view')


def add_days(start_date, added_days):
    global holidays
    global coronadays

    days_elapsed = 0
    while days_elapsed < added_days:
        test_date = start_date+dt.timedelta(days=1)
        start_date = test_date
        if test_date in holidays:
            continue
        else:
            days_elapsed += 1

    return start_date


def business_days(start_date, end_date):
    global holidays
    global coronadays

    days_elapsed = 0
    test_date = start_date

    if end_date > test_date:
        while test_date < end_date:
            test_date = test_date+dt.timedelta(days=1)
            if test_date in holidays:
                continue
            else:
                days_elapsed += 1

    return days_elapsed


def business_with_corona_days(start_date, end_date):
    days_elapsed = 0
    test_date = start_date

    if end_date > test_date:
        while test_date < end_date:
            test_date = test_date+dt.timedelta(days=1)
            if test_date in holidays and test_date not in coronadays:
                continue
            else:
                days_elapsed += 1

    return days_elapsed
