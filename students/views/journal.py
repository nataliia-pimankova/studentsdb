# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from calendar import monthrange, weekday, day_abbr

# Views for Journal
def journal(request):

    context = {}
    today = datetime.today()
    month = date(today.year, today.month, 1)

    next_month = month + relativedelta(months=1)
    prev_month = month - relativedelta(months=1)

    context['month_verbose'] = month.strftime('%B')
    context['year'] = month.year
    context['next_month'] = next_month.strftime('%Y-%m-%d')
    context['prev_month'] = prev_month.strftime('%Y-%m-%d')

    myear, mmonth = month.year, month.month
    number_of_days = monthrange(myear, mmonth)[1]
    context['month_header'] = [{'day': d,
                                'verbose': day_abbr[weekday(myear, mmonth, d)][:2]}
                               for d in range(1, number_of_days + 1)]

    journal = (
        {
            'id': 1,
            'student': 'Подоба Віталій',
            'attendance': ({'2': True,},
                           {'3': True,},
                           {'4': True,},
                           {'5': True,},
                           {'6': True,},
                           {'8': True,},
                           ),
        },
        {
            'id': 2,
            'student': 'Корост Андрій',
            'attendance': (
                {'3': True,},
                {'4': True,},
                {'5': True,},
                {'6': True,},
                {'10': True,},
                           ),
        },
        {
            'id': 3,
            'student': 'Притула Тарас',
            'attendance': (
                           {'4': True,},
                           {'5': True,},
                           {'9': True,},
                           ),
        },
    )
    return render(request, 'students/journal.html', {'journal': journal, 'context': context})
