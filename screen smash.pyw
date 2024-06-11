import ctypes 
import random
from random import randrange as xorshift32

#Coded by Viperine.

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32

def screen_smash():
    try:
        hdc = user32.GetDC(0x00)
        w = user32.GetSystemMetrics(0x00)
        h = user32.GetSystemMetrics(0x01)
        randomRop = [0x008800C6, 0x00CC0020, 0x00EE0086]
        user32.SetProcessDPIAware()
        while True:
             x = xorshift32(w)
             y = xorshift32(h)
             gdi32.BitBlt(hdc, x + xorshift32(0x21), y + xorshift32(0x21), 0x150, 0x150, hdc, x + xorshift32(0x21), y + xorshift32(0x21), random.choice(randomRop))
             kernel32.Sleep(0x10)
    except Exception as fail:
        print("Failed to start this GDI visual screen effect")
screen_smash()


