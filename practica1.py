import threading

num = 20

def worker(i):
    """funcion que realiza el trabajo en el thread"""
    print("Hola mundo " + str(i+1))
    return
threads = list()
for i in range(num):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()