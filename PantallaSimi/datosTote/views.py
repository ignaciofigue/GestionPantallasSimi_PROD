from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .models import Tote
from django.shortcuts import render
from django.db.models import Count
from collections import Counter
import matplotlib.pyplot as plt

@csrf_exempt
def datosTote(request):
      if request.method == 'POST':
        data = json.loads(request.body)
        
        # Extraer datos del JSON
        id_tote = data.get('id')
        codigo_tote = data.get('codigo')
        pallet_tote = data.get('pallet')
        peso_tote = data.get('peso')
        salida_tote = data.get('salida')
        destino_tote = data.get('destino')
        # Continuar extrayendo los demás campos según sea necesario

        # Guardar los datos en la base de datos
        objeto_nuevo = Tote(identificador=id_tote, codigo=codigo_tote, pallet=pallet_tote, peso=peso_tote, salida=salida_tote, destino=destino_tote)
        objeto_nuevo.save()

        return JsonResponse({'mensaje': 'Datos recibidos y guardados correctamente'})
      else:
        return JsonResponse({'error': 'Método no permitido'}, status=405)
      
# pallets_A = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7']
# pallets_A2 = ['A8', 'A9', 'A10', 'A11', 'A12', 'A13', 'A14']
# pallets_B = ['B1', 'B2', 'B3', 'B4', 'B5', 'B6', 'B7']
# pallets_B2 = ['B8', 'B9', 'B10', 'B11', 'B12', 'B13', 'B14']

def salida01(request):
   titulo_pagina = "Clasificador salida 01"
   totes = Tote.objects.filter(salida="1").order_by('-id')[:10][::-1]
   #total_por_pallet = Tote.objects.filter(salida="01").values('pallet').annotate(total_productos=Count('id')) 
   return render(request, 'salida1.html', {'objetos': totes, 'titulo_pagina': titulo_pagina})
   

def salida02(request):
   titulo_pagina = "Bultos clasificados en salida 02"
   totes = Tote.objects.filter(salida="2").order_by('-id')[:10][::-1]
   #total_por_pallet = Tote.objects.filter(salida="02").values('pallet').annotate(total_productos=Count('id')) 
   return render(request, 'salida.html', {'objetos': totes, 'titulo_pagina': titulo_pagina})

def salida03(request):
   titulo_pagina = "Bultos clasificados en salida 03"
   totes = Tote.objects.filter(salida="3").order_by('-id')[:10][::-1]
   #total_por_pallet = Tote.objects.filter(salida="03").values('pallet').annotate(total_productos=Count('id')) 
   return render(request, 'salida.html', {'objetos': totes, 'titulo_pagina': titulo_pagina})

def salida04(request):
   titulo_pagina = "Clasificador salida 02"
   totes = Tote.objects.filter(salida="4").order_by('-id')[:10][::-1]
   #total_por_pallet = Tote.objects.filter(salida="04").values('pallet').annotate(total_productos=Count('id')) 
   return render(request, 'salida4.html', {'objetos': totes, 'titulo_pagina': titulo_pagina})

def salida05(request):
   titulo_pagina = "Bultos clasificados en salida 05"
   totes = Tote.objects.filter(salida="05").order_by('-id')[:10][::-1]
   total_por_pallet = Tote.objects.filter(salida="05").values('pallet').annotate(total_productos=Count('id')) 
   return render(request, 'salida.html', {'objetos': totes, 'titulo_pagina': titulo_pagina,})

def destinos(request):
   ultimo_tote = Tote.objects.order_by('-id')[:5]
   datos = Tote.objects.all()
   salidas = [dato.salida for dato in datos]
   conteo_salidas = dict(Counter(salidas))

def landingPage(request):
   return render(request, 'landing2.html')

def ripley(request):
   return render(request, 'ripley.html')

def limpiar_bbdd(request):
   if request.GET.get('palabra_clave') == 'acm1pt':
   # Aquí va la lógica que deseas ejecutar
      Tote.objects.all().delete()
      return HttpResponse('La palabra clave es válida. Acción ejecutada.')
   else:
      return HttpResponse('La palabra clave es incorrecta.')
