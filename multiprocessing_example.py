# coding: utf-8

import multiprocessing
import os
import time


def calcul_long():
    n = 1E8
    while n > 0:
        n -= 1


def main():
    processes = []

    for i in range(4):
    #for i in range(os.cpu_count()):
        print(' registered processus %d' % i)

        th = multiprocessing.Process(target=calcul_long, args=())
        processes.append(th)

    t1_start = time.perf_counter()

    # lancement des threads
    for process in processes:
        process.start()

    # attente des threads
    for process in processes:
        process.join()

    t1_stop = time.perf_counter()

    print("Elapsed time in seconds:", t1_stop - t1_start)


if __name__ == '__main__':
    main()
