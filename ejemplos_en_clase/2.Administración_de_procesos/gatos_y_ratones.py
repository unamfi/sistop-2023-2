#!/usr/bin/python3
import threading
import time
import random

num_gatos = 5
num_ratones = 5
num_platos = 3

mutex_cuarto_g = threading.Semaphore(1)
mutex_cuarto_r = threading.Semaphore(1)
num_ratones_en_cuarto = 0
mutex_num_ratones = threading.Semaphore(1)
num_gatos_en_cuarto = 0
mutex_num_gatos = threading.Semaphore(1)
mutex_platos = [threading.Semaphore(1) for i in range(num_platos)]

def comiendo(yo, plato):
    global num_gatos, num_ratones
    print("%s Voy a comer del plato %d" % (yo, plato))
    with mutex_platos[plato]:
        print("%s Comiendo del plato %d; hay %d🐭/%d🐱 alrededor" %
              (yo, plato, num_ratones_en_cuarto, num_gatos_en_cuarto))
    time.sleep(random.random())
    print("%s Satisfecho. Me voy, dejo libre al plato %d" % (yo, plato))

def gato(n):
    global num_gatos_en_cuarto, num_ratones_en_cuarto
    print("😸%d nace" % n)
    while True:
        time.sleep(random.random())
        # Ahora sí tengo hambre...
        with mutex_num_gatos:
            if num_gatos_en_cuarto == 0:
                mutex_cuarto_g.acquire()
            num_gatos_en_cuarto += 1

        # with mutex_num_ratones:
        #     if num_ratones_en_cuarto > 0:
        #         print("🙀%d ¡UN RATÓN!" % n)
        #         print("😼%d Ni modo, me lo como..." % n)
        #         num_ratones_en_cuarto -= 1

        comiendo("😺%d" % n, random.randint(0,num_platos-1))

        with mutex_num_gatos:
            num_gatos_en_cuarto -= 1
            if num_gatos_en_cuarto == 0:
                mutex_cuarto_g.release()

def raton(n):
    global num_ratones_en_cuarto
    print("🐭%d nace" % n)
    while True:
        time.sleep(random.random())
        # Ahora sí tengo hambre...
        mutex_cuarto_g.acquire()
        with mutex_num_ratones:
            num_ratones_en_cuarto += 1
            # if num_ratones_en_cuarto == 1:
            #     mutex_cuarto_r.acquire()

        # Ojo, este acceso no está protegido por mutex.
        if num_gatos_en_cuarto > 0:
            print("🐭🪤😱 ¡¡¡¡¡UN GATO!!!!!")
        comiendo("🐭%d" % n, random.randint(0,num_platos-1))

        with mutex_num_ratones:
            num_ratones_en_cuarto -= 1
            # if num_ratones_en_cuarto == 0:
            #     mutex_cuarto_r.release()
        mutex_cuarto_g.release()

for i in range(num_ratones):
    threading.Thread(target=raton, args=[i]).start()

for i in range(num_gatos):
    threading.Thread(target=gato, args=[i]).start()
