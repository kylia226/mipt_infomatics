import threading


def worker():
    with lock:
        print(LIST.append('item'), LIST)
        LIST.append('item')
        print("1")


LIST = []
lock = threading.Lock()
if __name__ == "__main__":
    processes = [
        multiprocessing.Process(target=worker)
        for _ in range(5)
    ]

    for p in processes:
        p.start()
    for p in processes:
        p.join()
    print(LIST)
    
#процессы в list параллельны и изменения занимают разные участки памяти - не синхронизируются, поэтому изменения в list не отображаются
