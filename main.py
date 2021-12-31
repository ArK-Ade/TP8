# coding: utf-8

# Librairies
import os
import subprocess
import re
import threading
import time
import logging

"""
Cette fonction simule un calcul très long
"""


def calcul_long(name):
    logging.info("Thread %s: starting", name)
    n = 1E7
    while n > 0:
        n -= 1
    logging.info("Thread %s: finishing", name)


if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    logging.info("Main    : before creating thread")
    x = threading.Thread(target=calcul_long, args=(1,))
    logging.info("Main    : before running thread")
    x.start()
    logging.info("Main    : wait for the thread to finish")
    # x.join()
    logging.info("Main    : all done")



# TODO effectuer le multi threading et multi processing sur la fonction calcul_long()

# TODO Faire un programme qui construit et affiche une peinture avec des fourmis.
#  Les paramètres (page 205 du pdf) seront à mettre dans un fichier texte ou mieux XML.
#  En plus de dessiner une jolie peinture, l’objectif est de mettre en oeuvre la programmation asynchrone.

