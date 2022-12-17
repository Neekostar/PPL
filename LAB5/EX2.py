import threading
import time
from random import randint
from threading import Thread

resultList = []

lockObj = threading.Lock()


def rowGenerator(size, downLevel, upLevel):
    with lockObj:
        print(f"Поток {threading.current_thread().name} начал генерировать строку для матрицы")
        resultList.append([randint(downLevel, upLevel) for i in range(size)])
        time.sleep(1)
        print(f"Поток {threading.current_thread().name} закончил генерацию строки")


thread1 = threading.Thread(target=rowGenerator, args=(5, 10, 19,))
thread2 = threading.Thread(target=rowGenerator, args=(5, 20, 29,))
thread3 = threading.Thread(target=rowGenerator, args=(5, 30, 39,))
threads = [thread1, thread2, thread3]
for thread in threads:
    thread.start()
    thread.join()

for i in resultList:
    print(i)
