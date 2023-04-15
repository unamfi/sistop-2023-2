#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:41:48 2023

@author: Manases Leonel Oronzor Montes 

Problema: El cruce del rio
          
Instrucciones: Para llegar a un encuentro de desarrolladores de sistemas
               operativos, hace falta cruzar un río en balsa.
               Los desarrolladores podrían pelearse entre sí, hay que cuidar
               que vayan con un balance adecuado
               
               Reglas de negocio: En la balsa caben cuatro (y sólo cuatro) personas
                                  La balsa es demasiado ligera, y con menos de cuatro 
                                  puede volcar.
                                  Al encuentro están invitados hackers (desarrolladores de Linux)
                                  y serfs (desarrolladores de Microsoft).
                                  Para evitar peleas, debe mantenerse un buen balance: No
                                  debes permitir que aborden tres hackers y un serf, o tres serfs y
                                  un hacker. Pueden subir cuatro del mismo bando, o dos y dos.
                                  Hay sólo una balsa.
                                  No se preocupen por devolver la balsa (está programada para
                                  volver sola)
"""

import threading
import random
import time

mutex = threading.Semaphore(1)
hackers_sem = threading.Semaphore(0)
serfs_sem = threading.Semaphore(0)

hackers_count = 0
serfs_count = 0
boarded_count = 0

def hacker():
    global hackers_count, serfs_count
    mutex.acquire()
    hackers_count += 1
    print("Hacker llega al río.")
    if hackers_count == 4:
        for i in range(1,5):
            hackers_sem.release()
        hackers_count = 0
        print('**** 4 Hackers llegaron al río.')
    elif hackers_count == 2 and serfs_count == 2:
        hackers_sem.release()
        hackers_sem.release()
        serfs_sem.release()
        serfs_sem.release()
        hackers_count = 0
        serfs_count = 0
        print('**** 2 Hackers y 2 serfs llegaron al río.')
    else:
        mutex.release()

    hackers_sem.acquire()
    print("Hacker sube a la balsa.")
    global boarded_count
    boarded_count += 1
    if boarded_count == 4:
        print("~~~La balsa está llena.")
        time.sleep(0.5)
        print("###### La balsa llega al otro lado del río.######")
        boarded_count = 0
        mutex.release()

def serf():
    global hackers_count, serfs_count
    mutex.acquire()
    serfs_count += 1
    print("Serf llega al río.")
    if serfs_count == 4:
        for i in range(1,5):
            serfs_sem.release()
        serfs_count = 0
        print('***** 4 Serf llegaron al río.')
    elif serfs_count == 2 and hackers_count == 2:
        hackers_sem.release()
        hackers_sem.release()
        serfs_sem.release()
        serfs_sem.release()
        hackers_count = 0
        serfs_count = 0
        print('***** 2 Hackers y 2 serfs llegaron al río.')
    else:
        mutex.release()

    serfs_sem.acquire()
    print("Serf sube a la balsa.")
    global boarded_count
    boarded_count += 1
    if boarded_count == 4:
        print("~~~La balsa está llena.")
        time.sleep(0.5)
        print("###### La balsa llega al otro lado del río. ###### ")
        boarded_count = 0
        mutex.release()
        
while True:
      if random.randint(0, 1) == 0:
             threading.Thread(target=hacker,).start()
      else:
             threading.Thread(target=serf,).start()

