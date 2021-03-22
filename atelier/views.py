from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from asset.models import *
from atelier.models import *
from django.db.models import Max
import numpy as np
from datetime import datetime, date, timedelta, time
import itertools
import operator
from django.db.models import *
import random
from django.db.models import Count
import json

#from library.libs import *
import pandas as pd
#import xlsxwriter

def atelier(request):
	imersion_all = Imersion.objects.all()
	for el in imersion_all:
            el.delete()
	try:
		ganhos_euros = 125 + int(Imersion.objects.filter(Q(status = 'finalizada')).aggregate(Sum('gains_money'))['gains_money__sum'])
		ganhos_time = 210 + int(Imersion.objects.filter(Q(status = 'finalizada')).aggregate(Sum('gains_time'))['gains_time__sum'])
		total_imersoes = 25 + len(Imersion.objects.filter(Q(status = 'finalizada')).filter(Q(status = 'finalizada')))
	except:
		ganhos_euros = 0
		ganhos_time = 0
		total_imersoes = 0

	try:
		metier_convergencia_ganhos_euros = 0 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Convergência')).aggregate(Sum('gains_money'))['gains_money__sum'])
		metier_convergencia_ganhos_time = 0 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Convergência')).aggregate(Sum('gains_time'))['gains_time__sum'])
		metier_convergencia_total_imersoes = 0 + len(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Convergência')).filter(Q(status = 'finalizada')))
	except:
		metier_convergencia_ganhos_euros = 0
		metier_convergencia_ganhos_time = 0
		metier_convergencia_total_imersoes = 0
	try:
		metier_IFM_ganhos_euros = 0 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'IFM')).aggregate(Sum('gains_money'))['gains_money__sum'])
		metier_IFM_ganhos_time = 0 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'IFM')).aggregate(Sum('gains_time'))['gains_time__sum'])
		metier_IFM_total_imersoes = 0 + len(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'IFM')).filter(Q(status = 'finalizada')))
	except:
		metier_IFM_ganhos_euros = 0
		metier_IFM_ganhos_time = 0
		metier_IFM_total_imersoes = 0
	try:
		metier_carroceria_ganhos_euros = 0 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Carroceria')).aggregate(Sum('gains_money'))['gains_money__sum'])
		metier_carroceria_ganhos_time = 0 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Carroceria')).aggregate(Sum('gains_time'))['gains_time__sum'])
		metier_carroceria_total_imersoes = 0 + len(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Carroceria')).filter(Q(status = 'finalizada')))
	except:
		metier_carroceria_ganhos_euros = 0
		metier_carroceria_ganhos_time = 0
		metier_carroceria_total_imersoes = 0
	try:
		metier_pintura_ganhos_euros = 0 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Pintura')).aggregate(Sum('gains_money'))['gains_money__sum'])
		metier_pintura_ganhos_time = 0 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Pintura')).aggregate(Sum('gains_time'))['gains_time__sum'])
		metier_pintura_total_imersoes = 0 + len(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Pintura')).filter(Q(status = 'finalizada')))
	except:
		metier_pintura_ganhos_euros = 0
		metier_pintura_ganhos_time = 0
		metier_pintura_total_imersoes = 0
	try:
		metier_CVU_ganhos_euros = 20 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'CVU')).aggregate(Sum('gains_money'))['gains_money__sum'])
		metier_CVU_ganhos_time = 50 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'CVU')).aggregate(Sum('gains_time'))['gains_time__sum'])
		metier_CVU_total_imersoes = 4 + len(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'CVU')).filter(Q(status = 'finalizada')))
	except:
		metier_CVU_ganhos_euros = 20
		metier_CVU_ganhos_time = 50
		metier_CVU_total_imersoes = 4
	try:
		metier_proces_ganhos_euros = 15 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Processos CVP')).aggregate(Sum('gains_money'))['gains_money__sum'])
		metier_proces_ganhos_time = 35 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Processos CVP')).aggregate(Sum('gains_time'))['gains_time__sum'])
		metier_proces_total_imersoes = 3 + len(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Processos CVP')).filter(Q(status = 'finalizada')))
	except:
		metier_proces_ganhos_euros = 15
		metier_proces_ganhos_time = 35
		metier_proces_total_imersoes = 3
	try:
		metier_meios_ganhos_euros = 25 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Meios')).aggregate(Sum('gains_money'))['gains_money__sum'])
		metier_meios_ganhos_time = 50 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Meios')).aggregate(Sum('gains_time'))['gains_time__sum'])
		metier_meios_total_imersoes = 5 + len(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'Meios')).filter(Q(status = 'finalizada')))
	except:
		metier_meios_ganhos_euros = 25
		metier_meios_ganhos_time = 50
		metier_meios_total_imersoes = 5
	try:
		metier_CMO_ganhos_euros = 65 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'CMO')).aggregate(Sum('gains_money'))['gains_money__sum'])
		metier_CMO_ganhos_time = 75 + int(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'CMO')).aggregate(Sum('gains_time'))['gains_time__sum'])
		metier_CMO_total_imersoes = 13 + len(Imersion.objects.filter(Q(status = 'finalizada') & Q(metier = 'CMO')).filter(Q(status = 'finalizada')))
	except:
		metier_CMO_ganhos_euros = 65
		metier_CMO_ganhos_time = 75
		metier_CMO_total_imersoes = 13
	




	conta_mes = [3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for el in imersion_all:
		conta_mes[int(el.date[0:2]) - 1] = conta_mes[int(el.date[0:2]) - 1] + 1

	conta_taxa = [13, 12, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	for el in imersion_all:
		taxa_mes = el.date[0:2]
		conta_taxa[int(el.date[0:2]) - 1] = conta_taxa[int(el.date[0:2]) - 1] + int(el.duration) #taxa para 100h disponivel

	horas_total = 0
	data_atual = date.today()
	for el in conta_taxa:
		horas_total += el
	taxa_total = int(horas_total/((data_atual.month - 1) + (data_atual.day/30)))

	metier = ['Convergência', 'IFM', 'Carroceria', 'Pintura', 'CVU','Processos (CVP)','Meios (CVP)','CMO']
	conta_metier_qtd = [0 ,0, 0, 0, 4, 3, 5, 13]
	for el in imersion_all:
		contador = 0
		for met in metier:
			if met == el.metier:
				conta_metier_qtd[contador] += 1
			contador += 1

	conta_metier_ganhos_time = [0 ,0, 0, 0, 50, 35, 50, 75]
	for el in imersion_all:
		contador = 0
		for met in metier:
			if met == el.metier:
				conta_metier_ganhos_time[contador] = conta_metier_ganhos_time[contador] + int(el.gains_time)
			contador += 1

	conta_metier_ganhos_money = [0 ,0, 0, 0, 20, 15, 25, 65]
	for el in imersion_all:
		contador = 0
		for met in metier:
			if met == el.metier:
				conta_metier_ganhos_money[contador] = conta_metier_ganhos_money[contador] + int(el.gains_money)
			contador += 1

	conta_metier_qtd0 = int(conta_metier_qtd[0])
	conta_metier_qtd1 = int(conta_metier_qtd[1])
	conta_metier_qtd2 = int(conta_metier_qtd[2])
	conta_metier_qtd3 = int(conta_metier_qtd[3])
	conta_metier_qtd4 = int(conta_metier_qtd[4])
	conta_metier_qtd5 = int(conta_metier_qtd[5])
	conta_metier_qtd6 = int(conta_metier_qtd[6])
	conta_metier_qtd7 = int(conta_metier_qtd[7])
	
	
	context = {	"ganhos_time": ganhos_time,
	            "ganhos_euros": ganhos_euros,
	            "total_imersoes": total_imersoes,
	            "taxa_total": taxa_total,
	            "conta_metier_ganhos_money": conta_metier_ganhos_money,
	            "conta_metier_ganhos_time": conta_metier_ganhos_time,
	            "conta_metier_qtd": conta_metier_qtd,
	            "conta_mes": conta_mes,
	            "conta_taxa": conta_taxa,
	            "conta_metier_qtd0": conta_metier_qtd0,
	            "conta_metier_qtd1": conta_metier_qtd1,
	            "conta_metier_qtd2": conta_metier_qtd2,
	            "conta_metier_qtd3": conta_metier_qtd3,
	            "conta_metier_qtd4": conta_metier_qtd4,
	            "conta_metier_qtd5": conta_metier_qtd5,
	            "conta_metier_qtd6": conta_metier_qtd6,
	            "conta_metier_qtd7": conta_metier_qtd7,

	            "metier_convergencia_ganhos_euros": metier_convergencia_ganhos_euros,
	            "metier_convergencia_ganhos_time": metier_convergencia_ganhos_time,
	            "metier_convergencia_total_imersoes": metier_convergencia_total_imersoes,

	            "metier_IFM_ganhos_euros": metier_IFM_ganhos_euros,
	            "metier_IFM_ganhos_time": metier_IFM_ganhos_time,
	            "metier_IFM_total_imersoes": metier_IFM_total_imersoes,

	            "metier_carroceria_ganhos_euros": metier_carroceria_ganhos_euros,
	            "metier_carroceria_ganhos_time": metier_carroceria_ganhos_time,
	            "metier_carroceria_total_imersoes": metier_carroceria_total_imersoes,

	            "metier_pintura_ganhos_euros": metier_pintura_ganhos_euros,
	            "metier_pintura_ganhos_time": metier_pintura_ganhos_time,
	            "metier_pintura_total_imersoes": metier_pintura_total_imersoes,

	            "metier_CVU_ganhos_euros": metier_CVU_ganhos_euros,
	            "metier_CVU_ganhos_time": metier_CVU_ganhos_time,
	            "metier_CVU_total_imersoes": metier_CVU_total_imersoes,

	            "metier_proces_ganhos_euros": metier_proces_ganhos_euros,
	            "metier_proces_ganhos_time": metier_proces_ganhos_time,
	            "metier_proces_total_imersoes": metier_proces_total_imersoes,

	            "metier_meios_ganhos_euros": metier_meios_ganhos_euros,
	            "metier_meios_ganhos_time": metier_meios_ganhos_time,
	            "metier_meios_total_imersoes": metier_meios_total_imersoes,

	            "metier_CMO_ganhos_euros": metier_CMO_ganhos_euros,
	            "metier_CMO_ganhos_time": metier_CMO_ganhos_time,
	            "metier_CMO_total_imersoes": metier_CMO_total_imersoes,

	          }
	return render(request, 'atelier/templates/atelier.html', context)


def reserva(request):
	imersion_all = Imersion.objects.all()
	if request.method == 'POST' and request.POST.get('ORIGIN') == 'reservando':
            imersion_all = Imersion()
            test = Points()
            print(test)
            imersion_all.title = request.POST.get('title')
            imersion_all.cami = request.POST.get('cami')
            imersion_all.pfi = request.POST.get('pfi')
            imersion_all.metier = request.POST.get('metier')
            imersion_all.time_initial = request.POST.get('time_initial')
            imersion_all.date = request.POST.get('date')
            imersion_all.duration = int(request.POST.get('duration'))
            imersion_all.status = "reservada"
            imersion_all.gains_time = 0
            imersion_all.gains_money = 0
            imersion_all.description = "Ainda não há descrição"
            imersion_all.save()
            print('passou aquiiiiiiiiiiiiiiiiiiiiiiiii')
            return redirect('reserva')
	context = {"imersion_all":imersion_all}
	return render(request, 'atelier/templates/reserva.html', context)

def finaliza(request, id):
	finaliza_imersion = Imersion.objects.get(id = id)
	if request.method == 'POST' and request.POST.get('ORIGIN') == 'finalizando':
		finaliza_imersion.status = "finalizada"
		finaliza_imersion.gains_money = request.POST.get('gains_money')
		finaliza_imersion.gains_time = request.POST.get('gains_time')
		finaliza_imersion.description = request.POST.get('description')
		finaliza_imersion.save()
	context = {"id": id, "finaliza_imersion": finaliza_imersion}
	return render(request, 'atelier/templates/finaliza.html', context)

def galeria(request):
    context = {}
    return render(request, 'atelier/templates/galeria.html', context)