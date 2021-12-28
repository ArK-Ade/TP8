# coding: utf-8

# Librairies
import os
import subprocess
import re
import threading

"""
Cette fonction simule un calcul très long
"""


def calcul_long():
    n = 1E7
    while n > 0:
        n -= 1


# TODO effectuer le multi threading et multi processing sur la fonction calcul_long()

# TODO Faire un programme qui construit et affiche une peinture avec des fourmis.
#  Les paramètres (page 205 du pdf) seront à mettre dans un fichier texte ou mieux XML.
#  En plus de dessiner une jolie peinture, l’objectif est de mettre en oeuvre la programmation asynchrone.

print("hello")
