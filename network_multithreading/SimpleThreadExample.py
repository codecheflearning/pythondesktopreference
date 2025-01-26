from threading import Thread
import random
import string
from time import sleep

def print_word():
    for _ in range(10):
        letters = string.ascii_letters
        word = "".join(random.choice(letters) for i in range(random.randint(4, 10)))
        print(word)
        sleep(random.randint(1, 3))

def print_number():
    for _ in range(10):
        num = random.randint(10, 100)
        print(str(num))
        sleep(random.randint(1, 3))


t = Thread(target=print_number)
t.start()

t = Thread(target=print_word)
t.start()

t.join()

