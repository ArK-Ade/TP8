# coding: utf-8

# Librairies
import threading
import multiprocessing

import os
import math
import asyncio
import time
import sys
import itertools


class Signal:
    go = True


"""
Cette fonction simule un calcul très long
"""

nombre_final = 100000.0


def calcul_long():
    print(f"started at {time.strftime('%X')}")
    n = 1E7
    while n > 0:
        n -= 1
    print(f"finished at {time.strftime('%X')}")
    print("nombre final " + str(n))


def calcul_longV2(signal):
    global nombre_final
    if nombre_final > 0:
        nombre_final -= 1
    else:
        signal.go = False


def calcul_long_multi_thread():
    print(f"started at {time.strftime('%X')}")
    threads = []
    signal = Signal()

    # boucle
    while signal.go:

        # creation du tableau
        for i in range(os.cpu_count()):
            # print(' registered thread %d' % i)

            th = threading.Thread(target=calcul_longV2, args=(signal,))
            threads.append(th)

        # lancement des threads
        for thread in threads:
            thread.start()

        # synchronisation
        for thread in threads:
            thread.join()

        threads.clear()

    print(f"finished at {time.strftime('%X')}")
    print("nombre final " + str(nombre_final))
    print("active count : " + str(threading.active_count()))


def calcul_long_multi_processing():
    pass


# TODO effectuer le multi threading et multi processing sur la fonction calcul_long()

# TODO Faire un programme qui construit et affiche une peinture avec des fourmis.
#  Les paramètres (page 205 du pdf) seront à mettre dans un fichier texte ou mieux XML.
#  En plus de dessiner une jolie peinture, l’objectif est de mettre en oeuvre la programmation asynchrone.


print("Debut du programme")
calcul_long()
# calcul_long_multi_thread()
calcul_long_multi_thread()
