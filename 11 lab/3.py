import threading
import time
from random import randint

start = time.time()


def multithreading_summation(arr):
    def thread_job(index, count):
        with lock:
            global summ
            for i in range(index, index + count):
                summ += arr[i]

    threads = [threading.Thread(target=thread_job, args=(i * 10 ** 5, 10 ** 5)) for i in range(10)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    print(summ)


arr = [randint(0, 10 ** 8) for i in range(10 ** 6)]

lock = threading.Lock()
summ = 0
multithreading_summation(arr)
print(time.time() - start)

#примерно одинаковое время, за счет рандомизации оно смещается

#пример вывода:
49991114729921
2.5767059326171875
