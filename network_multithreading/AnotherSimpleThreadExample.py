import threading
from threading import Thread
import random
from time import sleep

def print_number(*values):
    for num in values:
        print(f"Thread Name: {threading.current_thread().name} {num}")
        sleep(random.randint(1, 3))


t = Thread(name = 'Named Thread', target=print_number, args = [random.randint(10, 100) for _ in range(20)])
t.start()

t = Thread(target=print_number, args = [random.randint(10, 100) for _ in range(20)])
t.start()


