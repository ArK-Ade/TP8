# coding: utf-8

import threading
import os
import time


def calcul_long():
    n = 1E8
    while n > 0:
        n -= 1


def main():
    threads = []

    for i in range(4):
    #for i in range(os.cpu_count()):
        print(' registered thread %d' % i)

        th = threading.Thread(target=calcul_long, args=())
        threads.append(th)

    t1_start = time.perf_counter()

    # lancement des threads
    for thread in threads:
        thread.start()

    # attente des threads
    for thread in threads:
        thread.join()

    t1_stop = time.perf_counter()

    print("Elapsed time in seconds:", t1_stop - t1_start)


if __name__ == '__main__':
    main()
