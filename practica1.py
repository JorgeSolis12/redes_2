#!/usr/bin/env python
# -*- coding: utf-8 -*-

import threading

#Listas con las palabras con sus variantes
alegria = {Alegría,Alegria,alegria, ALEGRIA, ALEGRÍA}
amor = {Amor, AMOR, amor}
ira = {IRA, Ira, ira}
frustracion ={frustracion, frustración, Frustración, FRUSTRACIÓN, FRUSTRACION}
estres = {estres, estrés, ESTRES, Estres}
enojo = {enojo, ENOJO, Enojo}

#Cambiar el número para el número de hilos
num = 1

#funcion para crear hilos
def worker(i):
    repetidas_enojo = 0
    repetidas_frust = 0
    repetidas_estres = 0
    repetidas_amor = 0
    repetidas_ira = 0
    repetidas_alegria = 0

    print("Hola mundo " + str(i+1))
    dir = "/home/jorgesolis/redes_2/libros/"+str(i+1)+".txt"
    archivo = open(dir, "r")
    for linea in archivo.readlines():
        print (linea) 
    archivo.close()
    return

threads = list()
for i in range(num):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()