from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import Http404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from asset.models import *
from django.db.models import Max
import numpy as np
from datetime import datetime, date, timedelta
import itertools
import operator
from django.db.models import *
import random
from django.db.models import Count
import json
#from conf.models import *
#import speech_recognition as sr

#from library.libs import *
import pandas as pd
#import xlsxwriter


#  pgadmin email: martins.georgesilva@gmail.com senha: 1234qwer


@login_required(login_url="login/")
def index(request):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    local = Points.objects.all()
    print(local)
    ficha = Measure()
    r = sr.Recognizer()
    with sr.Microphone() as source:
        while True:
            print("Speak Anything :")
            if request.method == 'POST' and request.POST.get('ORIGIN') == 'save_data': 
               print('AAARRRRPPPPPPPP¨¨¨¨¨¨¨¨¨¨666666666666666666677777778888888888888888888888888')

               context = {}
               return render(request, 'asset/templates/index.html', context)
            audio = r.listen(source)

                
            try:
                text = r.recognize_google(audio)
            except:
                text = 99
                print(text)
            try:
                if text == 'next':
                    #workbook = xlsxwriter.Workbook('file.xlsx')
                    #worksheet = workbook.add_worksheet()
                   
                    #worksheet.write(3, 0, text)
                    #workbook.close()
                    measure = 77
                #####AQUI COLOCAR OS COMANDOS#################
                else:
                    measure = float(text)
            except:
                measure = 666
            if measure:
                ficha.value_measure = measure
                ficha.save()
                print("You said : {}".format(text))
                print('rrrrrrrrrrrr')
                print(ficha.value_measure)
                print('tttttttttttt')
                table_measure = Measure.objects.all()
                print(table_measure)
                cliente = Measure.objects.last()
                print(cliente.value_measure)
                print('aaaaaaaaaaaaaabbbbb')

                #gravação do dado na planilha do excel. Pip install xlsxwriter
                workbook = xlsxwriter.Workbook('file.xlsx')
                worksheet = workbook.add_worksheet()
                worksheet.write(2, 3, cliente.value_measure)
                worksheet.write(3, 0, 'gustavo')
                workbook.close()

                context = {"measure": measure, "ficha": ficha, "cliente": cliente, "local": local }
                return render(request, 'asset/templates/index.html', context)
            else:
                print('yyyyyyyyyyyyyyyyyyyyyyyy')
            context = { "text": text, "local": local}
            return render(request, 'asset/templates/index.html', context)


'''
            try:
                text = r.recognize_google(audio)
                measure = float(text)
                ficha.value_measure = measure
                ficha.save()
                print("You said : {}".format(text))
                if measure:
                    print('rrrrrrrrrrrr')
                    print(ficha.value_measure)
                    print('tttttttttttt')
                    cliente = Measure.objects.last()
                    print(cliente.value_measure)
                    print('aaaaaaaaaaaaaabbbbb')
                    context = {"measure": measure, "ficha": ficha, "cliente": cliente}
                    return render(request, 'asset/templates/index.html', context)

            except:
                print("Sorry could not recognize what you said")
'''


@login_required(login_url="login/")
def index_1(request):
    print('aaaaaaaaaaaaaaaaaaaaaahhhhhhhhhhhaaaaaaaaaa')
    ficha = Measure()
    #cliente = Measure.objects.last()
    #print(cliente.value_measure)
    context = {}
    return render(request, 'asset/templates/index_1.html', context)


@login_required(login_url="login/")
def option(request):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    ficha = Measure()
    context = {}
    return render(request, 'asset/templates/option.html', context)



@login_required(login_url="login/")
def conf(request):
    print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    local = Points.objects.all()
    #local.delete()    
    if request.method == 'POST' and request.POST.get('ORIGIN') == 'partner':
        new = Points()
        new.Point = request.POST.get('name')
        new.imagem = request.POST.get('imagem')
        new.Cell = request.POST.get('celula')
        new.save()
        a = Points.objects.last()
        print (a.Point)
        print(a.imagem)
        print(a.Cell)
        print('XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
        return redirect('conf')
    context = {"local": local}
    return render(request, 'asset/templates/conf.html', context)


'''

@login_required(login_url="login/")
def view(request):
    context = {
  
    }
    return render(request, 'asset/templates/dash_cliente.html', context)



@login_required(login_url="login/")
def save_data(request, id): # GRAVA OS DADOS NO BANCO DE DADOS E EXCEL
    if request.method == 'POST': 
        colab = hse_fun_terceiro.objects.get(id=id)
        colab.nome_funcionario = request.POST.get('nome')
        colab.rg = request.POST.get('rg')
        colab.cpf = request.POST.get('cpf')
        colab.funcao = request.POST.get('funcao')
        colab.email = request.POST.get('email')
        colab.save()
        return redirect('contributors')
    return redirect('home')






@login_required(login_url="login/")
def VarialbleMonitored(request):
    _user = CurrentUserInfo(request.user.id) # _user[0] herda models User ; _user[1] herda models clientes  
    id_list = [el.id for el in _user[2]]
    variable_verification = variable.objects.filter(device__in=id_list)
    print(variable_verification)
    variable_auth = True if request.GET["Query"] in ''.join(str(variable_verification)) else None
    if variable_auth:
        var = variable.objects.get(name=request.GET["Query"])
        context = {
            'variableID':var.id,
        }
        return render(request, 'asset/templates/variable.html', context)
    else:
        return HttpResponse('Alguma Coisa saiu errado!!!')


def Ajax(request):
    values = get_data(request.GET["Arg"],request.GET["id"])
    print(values)
    ValuesChart01 = {
        "valores": values[0]
            }
    middleArr = []
    minArr = []
    maxArr  = []
    middleValue = round(np.mean(values[0]), 2)
    minutesValue = round(np.min(values[0]), 2)
    MaximumValue = round(np.max(values[0]), 2)
    for el in range(len(values[0])):
        middleArr.append(middleValue)
        minArr.append(minutesValue)
        maxArr.append(MaximumValue)
    AverageChart01={
        "valores": middleArr
            }
    MinChart01={
        "valores": minArr
            }
    MaxChart01={
        "valores": maxArr
            }
    LabelsChart01 = {
        "valores": values[1]
            }
    ConfVars = AssetMonitoredInfo.objects.last()
    var = 123
    Ymin = minutesValue*100
    Ymax = MaximumValue*100
   
    auxmin = Ymin % 2
    auxmax = Ymax % 2
    if auxmin != 0:
        Ymin -= 5
    if auxmax != 0:
        Ymax += 5   

    Ymin01 = Ymin/100
    Ymax01 = Ymax/100   
    context ={
        "label": 'Pressão - '+request.GET["Arg"],
        "ValData01": ValuesChart01,
        "ValData02": AverageChart01,
        "ValData03": MinChart01,
        "ValData04": MaxChart01,
        "ValLabels": LabelsChart01,
        'valor_minimo': minutesValue,
        'valor_medio': middleValue,
        'valor_maximo': MaximumValue,
        "EngUnit":'bar',
        'gauge_minino':0,
        'gauge_maximo':16,
        'gaugeLast':'2019-02-05 16:45',
        'gaugeValor':14,
        'last':3.33,
        'Ymin01':Ymin01,
        'Ymax01':Ymax01,
    }
    return HttpResponse(json.dumps(context))


def lastValueRealTimeChart(request):
    value = get_data('real', 5)
    context ={
        'last':value[0],

    }
    return HttpResponse(json.dumps(context))



def mensal(request):    
    agora = datetime.now()
    mes_atraz = datetime.now()
    mes_atraz -= timedelta(days=7)
    addTime = mes_atraz
    
    for el in range(60000):
        data = novatabela()  
        n = random.randint(0,3)
        data.valor = n
        addTime += timedelta(minutes=10)
        data.datahora = addTime
        data.save()



    return render(request, 'asset/templates/mensal.html', context)

'''