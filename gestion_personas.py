# -*- coding: utf-8 -*-
"""
Created on Mon May  6 15:48:06 2024

@author: Dell
"""

import os


def eliminar_archivo(nombre):
    os.remove(nombre)

def agregar_personas(nombre, contenido):
    archivo = open(nombre,"at")
    archivo.write("\n" + contenido)
    archivo.close()

def listar_personasDNI():
    nombre = "dni.txt"
    archivo = open(nombre,"rt")
    contenido = archivo.read()
    return contenido
def listar_personasNOM():
    nombre = "nombre.txt"
    archivo = open(nombre,"rt")
    contenido = archivo.read()
    return contenido
def listar_personasAPE():
    nombre = "apellido.txt"
    archivo = open(nombre,"rt")
    contenido = archivo.read()
    return contenido
