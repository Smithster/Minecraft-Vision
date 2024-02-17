import numpy
import pandas

from mss import mss
import cv2
import tensorflow
import PIL
import win32gui
import win32con
import win32ui
import win32api
import time


hwnd = win32gui.FindWindow(None, r'Minecraft 1.20.4 - Singleplayer')
hwndchild = win32gui.FindWindowEx(hwnd, None, r'Minecraft 1.20.4 - Singleplayer', None)
win32gui.SetForegroundWindow(hwnd)
win = win32ui.CreateWindowFromHandle(hwnd)
# left, top, right, bottom
dimensions = win32gui.GetWindowRect(hwnd)
print(hwnd)
yBuffer = 20
xBuffer = 11
with mss() as sct:
    # Part of the screen to capture
    # TODO - automatically grab the minecraft window
    monitor = {"top": dimensions[1], "left": dimensions[0], "width": dimensions[2] - dimensions[0], "height": dimensions[3] - dimensions[1]}

    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img)
        print(monitor)
        win.SendMessage(win32con.WM_KEYDOWN, win32con.VK_SPACE)
        win.SendMessage(win32con.WM_KEYDOWN, 0x57)
        win.SendMessage(win32con.WM_MOUSEMOVE, 1, win32api.MAKELONG(int(monitor["width"] / 2) - xBuffer, int(monitor["height"] / 2) - yBuffer))
        # win32gui.SendMessage(hwndchild, win32api.send, 1, win32api.MAKELONG(0,10))
        # print(test)

        # Display the picture in grayscale
        # cv2.imshow('OpenCV/Numpy grayscale',
        #            cv2.cvtColor(img, cv2.COLOR_BGRA2GRAY))

        # print(f"fps: {1 / (time.time() - last_time)}")

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break