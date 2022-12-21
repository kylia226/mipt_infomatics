import threading
import random
import time
import sys


def thread_job():
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()


counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)

#1 2 3 1 2 2 2 3 3 3 3 - за счет рандомизации времени по разным потокам, они "выбрасывают" значения в разное время, обгоняя друг друга

Решение:
import threading
import random
import time
import sys


def thread_job():
    lock.acquire()  # mutex
    global counter
    old_counter = counter
    time.sleep(random.randint(0, 1))
    counter = old_counter + 1
    print('{} '.format(counter), end='')
    sys.stdout.flush()
    lock.release() #Отсутствие строчки lock.release() может повесить остальные потоки в бесконечное ожидание

lock = threading.Lock()
counter = 0
threads = [threading.Thread(target=thread_job) for _ in range(10)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print(counter)
