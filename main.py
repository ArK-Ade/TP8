# coding: utf-8

# Librairies
import asyncio
import time


async def main():
    global nombre_final

    print(f"started at {time.strftime('%X')}")

    # Wait until both tasks are completed (should take
    # around 2 seconds.)

    groupe = await asyncio.gather(
        calcul_longV2(),
    )
    print(groupe)

    print(f"finished at {time.strftime('%X')}")
    print(groupe)


"""
Cette fonction simule un calcul très long
"""

nombre_final = 1E7


def calcul_long():
    print(f"started at {time.strftime('%X')}")
    n = 1E7
    while n > 0:
        n -= 1
    print(f"finished at {time.strftime('%X')}")
    print("nombre final " + str(n))


def calcul_longV2():
    global nombre_final
    nombre_final -= 1
    print(nombre_final)


def calcul_long_multi_thread():
    pass


def calcul_long_multi_processing():
    pass


# TODO effectuer le multi threading et multi processing sur la fonction calcul_long()

# TODO Faire un programme qui construit et affiche une peinture avec des fourmis.
#  Les paramètres (page 205 du pdf) seront à mettre dans un fichier texte ou mieux XML.
#  En plus de dessiner une jolie peinture, l’objectif est de mettre en oeuvre la programmation asynchrone.

print("Debut du programme")

asyncio.run(main())

# calcul_long()
# calcul_long_multi_thread()
