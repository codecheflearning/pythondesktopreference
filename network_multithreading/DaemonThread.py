import psutil
import shutil
from threading import Thread
import threading
from time import sleep

#Daemon thread example to monitor CPU, Memory and Disk Usage every 5 seconds
def monitor():
    print(f"Thread Name: {threading.current_thread().name}")
    while True: #infinite loop
        try:
            # Get CPU usage
            cpu_percent = psutil.cpu_percent()
            print(f"CPU Usage: {cpu_percent}%")
            # Get memory usage
            memory = psutil.virtual_memory()
            print(f"Total Memory: {memory.total / (1024 ** 3):.2f} GB")
            print(f"Available Memory: {memory.available / (1024 ** 3):.2f} GB")
            print(f"Used Memory: {memory.used / (1024 ** 3):.2f} GB")
            print(f"Memory Percentage: {memory.percent}%")
            total, used, free = shutil.disk_usage("/")
            print(f"Disk usage:")
            print(f"Total: {total // (2**30)} GB")
            print(f"Used: {used // (2**30)} GB")
            print(f"Free: {free // (2**30)} GB")
            print("|--------------------------------------------------|")
            print()
            sleep(1)
        except Exception as e:
                print(f"Exception in daemon thread: {e}")

if __name__ == "__main__": #Check if we are in main thread
    t = Thread(daemon = True, name = 'Daemon Thread', target=monitor)
    print("Main Thread start")
    t.start()
    sleep(6) #block main thread to run for 6 seconds
    print("Main Thread exiting")