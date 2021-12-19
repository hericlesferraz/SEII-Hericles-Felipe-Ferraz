#!/usr/bin/ýthon3

import time
import threading

def funcao(msg, num):
    for i in range(num):
        print(msg)
        time.sleep((0.5))

t_1 = threading.Thread(target=funcao, args=("primeira", 5))
t_2 = threading.Thread(target=funcao, args=("segunda", 5))
t_3 = threading.Thread(target=funcao, args=("terceira", 10))

t_1.start()
t_2.start()
t_3.start()

t_1.join()
t_2.join()
t_3.join()