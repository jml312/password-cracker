import pyautogui as pg
from time import sleep
from itertools import product
import string

pg.PAUSE = 0.000001


def countdown(start=5):
    for i in range(start, 0, -1):
        print("Starting in", i)
        sleep(1)
    print("Let's get cracking ...\n")


def get_progress():
    with open("progress.txt", "r") as f:
        n, progress = f.readline().split()
        return int(n), int(progress)


def write_progress(n, progress):
    with open("progress.txt", "w") as f:
        f.write(f"{n} {progress}")


def crack_number(n, progress=1):
    chars = string.ascii_lowercase + string.digits + " "
    guesses = list(product(chars, repeat=n))
    n_guesses = len(guesses) - 1
    countdown()
    for guess in guesses[progress:]:
        try:
            guess = ''.join(guess)
            print(f"{progress}/{n_guesses} - {guess}")
            progress += 1
            pg.write(guess)
            pg.press('enter')
        except KeyboardInterrupt:
            print("Keyboard interrupt")
            write_progress(n, progress - 1)
            break


n, progress = get_progress()
crack_number(n, progress)
