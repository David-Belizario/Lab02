from django.shortcuts import render
from django.http import HttpResponse
import math

# Create your views here.


def index(request):
    context = {
        'titulo': "Formulario",
    }
    return render(request, 'encuesta/formulario.html', context)

def enviar(request):
    context={
        
        'titulo': "Respuesta",
        'nombre': request.POST['nombre'],
        'clave': request.POST['password'],
        'educacion': request.POST['educacion'],
        'nacionalidad': request.POST['nacionalidad'],
        'idiomas': request.POST.getlist('idiomas'),
        'correo': request.POST['email'],
        'website': request.POST['sitioweb']
    }
    
    return render(request, 'encuesta/respuesta.html', context)

def calcular(request):
    if request.method == 'POST':
        numero1 = int(request.POST['numero1'])
        numero2 = int(request.POST['numero2'])
        operacion = request.POST['operacion']
        
        if operacion == 'suma':
            resultado = numero1 + numero2
            operacion_simbolo = '+'
        elif operacion == 'resta':
            resultado = numero1 - numero2
            operacion_simbolo = '-'
        elif operacion == 'multiplicacion':
            resultado = numero1 * numero2
            operacion_simbolo = '*'
        
        context = {
            'numero1': numero1,
            'numero2': numero2,
            'operacion': operacion,
            'operacion_simbolo': operacion_simbolo,
            'resultado': resultado,
        }
        
        return render(request, 'encuesta/resultado.html', context)
    
    return render(request, 'encuesta/calculadora.html')

def volumen_cilindro(request):
    if request.method == 'POST':
        altura = float(request.POST['altura'])
        diametro = float(request.POST['diametro'])
        radio = diametro / 2
        volumen = math.pi * (radio ** 2) * altura
        
        context = {
            'altura': altura,
            'diametro': diametro,
            'volumen': volumen,
        }
        
        return render(request, 'encuesta/resultado_volumen.html', context)
    
    return render(request, 'encuesta/formulario_volumen.html')