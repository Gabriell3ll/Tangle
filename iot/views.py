from django.shortcuts import render
from iot.models import Sensordata
from django.http import HttpResponse
import xlwt
# Create your views here.

def inicio(request): 
    return render(request,'dashboard.html')

def Presion(request):
    valorpresion=Sensordata.objects.last()
    valorpresiontodo=Sensordata.objects.all()
    valorpresiones=Sensordata.objects.all().order_by('-id')[:20:-1]
    return render(request,'Presion.html',{"valorpresion":valorpresion.presion,"valorpresiones":[x.presion for x in valorpresiones],"etipresion":valorpresiones,"valorpresiontodo":valorpresiontodo})

def Presion2(request):
    valorpresion=Sensordata.objects.last()
    valorpresiones=Sensordata.objects.all().order_by('-id')[:20:-1]
    return render(request,'Presion2.html',{"valorpresion":valorpresion.presion,"valorpresiones":[x.presion for x in valorpresiones],"etipresion":valorpresiones})

def Temperatura(request): 
    valortemperatura=Sensordata.objects.last()
    valortemperaturatodo=Sensordata.objects.all()
    valortemperaturas=Sensordata.objects.all().order_by('-id')[:20:-1]
    return render(request,'Temperatura.html',{"valortemperatura":valortemperatura.temperatura,"valortemperaturas":[x.temperatura for x in valortemperaturas],"etitemperatura":valortemperaturas,"valortemperaturatodo":valortemperaturatodo})

def Temperatura2(request): 
    valortemperatura=Sensordata.objects.last()
    valortemperaturas=Sensordata.objects.all().order_by('-id')[:20:-1]
    return render(request,'Temperatura2.html',{"valortemperatura":valortemperatura.temperatura,"valortemperaturas":[x.temperatura for x in valortemperaturas],"etitemperatura":valortemperaturas})
    
def Humedad(request):
    valorhumedad=Sensordata.objects.last()
    valorhumedadtodo=Sensordata.objects.all()
    valorhumedads=Sensordata.objects.all().order_by('-id')[:20:-1]
    return render(request,'Humedad.html',{"valorhumedad":valorhumedad.humedad,"valorhumedads":[x.humedad for x in valorhumedads],"etihumedad":valorhumedads,"valorhumedatodo":valorhumedadtodo})

def Humedad2(request): 
    valorhumedad=Sensordata.objects.last()
    valorhumedads=Sensordata.objects.all().order_by('-id')[:20:-1]
    return render(request,'Humedad2.html',{"valorhumedad":valorhumedad.humedad,"valorhumedads":[x.humedad for x in valorhumedads],"etihumedad":valorhumedads}) 

def export_xls(request):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="Datos.xls"'
 
    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('Datos')
 
    # Sheet header, first row
    row_num = 0
 
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
 
    columns = ['Fecha','Hora','Presion (Pa)','Temperatura (°C)','Humedad (%)']
 
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)
 
    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()
 
    rows = data=Sensordata.objects.all().values_list('fecha','hora','presion','temperatura','humedad')
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)
 
    wb.save(response)
    return response