import threading
import time


def count_a(name, limit, interval):
    print(f"{name} Starts Counting...")
    
    for i in range(limit):
        time.sleep(interval)
        print(f"{name} > {i}")


th1 = threading.Thread(target=count_a, args=["Counter_1", 14, 0.5])
th2 = threading.Thread(target=count_a, args=["Counter_2", 11, 1])

th1.start()
th2.start()
