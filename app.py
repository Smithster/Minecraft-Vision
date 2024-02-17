import numpy
from mss import mss
import cv2
import win32gui
import win32con
import win32ui
import win32api
import time
from inputs import inputs

hwnd = win32gui.FindWindow(None, r'Minecraft 1.20.4 - Singleplayer')
hwndchild = win32gui.FindWindowEx(hwnd, None, r'Minecraft 1.20.4 - Singleplayer', None)
win32gui.SetForegroundWindow(hwnd)
win = win32ui.CreateWindowFromHandle(hwnd)
# left, top, right, bottom
dimensions = win32gui.GetWindowRect(hwnd)
print(hwnd)

# Instatiates the inputs class for controlling the game
inputs = inputs(win, dimensions)

monitor = {"top": dimensions[1], "left": dimensions[0], "width": dimensions[2] - dimensions[0], "height": dimensions[3] - dimensions[1]}
cursorAccelerationX: int
cursorAccelerationY: int

cursorAccelerationX = 0
cursorAccelerationY = 0

with mss() as sct:
    # Part of the screen to capture
    # TODO - automatically grab the minecraft window
    while "Screen capturing":
        last_time = time.time()

        # Get raw pixels from the screen, save it to a Numpy array
        img = numpy.array(sct.grab(monitor))

        # Display the picture
        cv2.imshow("OpenCV/Numpy normal", img)
        # win.SendMessage(win32con.WM_KEYDOWN, win32con.VK_SPACE)
        # inputs.pressKey(' ')
        inputs.moveMouseAbsolute(cursorAccelerationX, cursorAccelerationY)

        # Press "q" to quit
        if cv2.waitKey(25) & 0xFF == ord("q"):
            cv2.destroyAllWindows()
            break