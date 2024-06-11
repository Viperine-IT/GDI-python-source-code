import ctypes 

#Coded by Viperine.

user32 = ctypes.windll.user32
gdi32 = ctypes.windll.gdi32
kernel32 = ctypes.windll.kernel32

def memz_inversion():
    try:
       hdc = user32.GetDC(0x00)
       w = user32.GetSystemMetrics(0x00)
       h = user32.GetSystemMetrics(0x01)
       user32.SetProcessDPIAware()
       while True:
           gdi32.PatBlt(hdc, 0, 0, w, h, 0x005A0049)
           kernel32.Sleep(0x50)
    except Exception as fail:
       print("Failed to start this GDI visual screen effect.")
memz_inversion()
