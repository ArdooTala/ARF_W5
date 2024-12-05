import threading
import time


def count_a(limit):
    print("Counting...")

    for i in range(limit):
        time.sleep(1)

        print(f"i = {i}")

        if i == 3:
            e.set()
        
        if i == 7:
            e.set()


e = threading.Event()

th1 = threading.Thread(target=count_a, args=[20])
th1.start()

print("Waiting for the event again on the MAIN THREAD")
e.wait()
print(">>> Beacons of Minas Tirith are lit...and MAIN THREAD will answer (by printing this line!)")
e.clear()

# Alternative Approach:
print("Starting the while loop on the MAIN THREAD")
while True:
    if e.is_set():
        print(">>> Event is finally set...")
        e.clear()
        break
    
    print("Event is not set yet...")
    time.sleep(0.3)

print("The while loop on the MAIN THREAD finished")
