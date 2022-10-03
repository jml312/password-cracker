import pyautogui as pg
from time import sleep
from itertools import product
import string

pg.PAUSE = 0.000001

for i in range(5, 0, -1):
    print("Starting in", i)
    sleep(1)
print("Let's get cracking ...\n")

chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + " "
low, high = 1, 6
for password_length in range(low, high):
    lengths = [37, 1_369, 50_653, 1_874_161, 69_343_957]
    count = 1
    for guess in product(chars, repeat=password_length):
        print(f"{count}/{lengths[password_length]} - {''.join(guess)}")
        count += 1
        guess = ''.join(guess)
        pg.write(guess)
        pg.press('enter')