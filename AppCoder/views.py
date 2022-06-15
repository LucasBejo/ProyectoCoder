from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Curso
# Create your views here.


def curso(self):
    curso = Curso(nombre="pogo",camada="0123")
    curso.save()
    documento = f"El curso es: {curso.nombre},la camada: {curso.camada}"
    return HttpResponse(documento)
