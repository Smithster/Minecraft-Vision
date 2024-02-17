import win32con
import win32api

## few magic number to find the middle of the screen (possibly because of outer rect area)
yBuffer = 19
xBuffer = 8

class inputs:
    def __init__(self, win, dimensions):
        self.win = win
        self.dimensions = dimensions
        self.basePosition = {
            "x": int((dimensions[2] - dimensions[0]) / 2) - xBuffer,
            "y": int((dimensions[3] - dimensions[1]) / 2) - yBuffer,
        }

    # Little side note but make sure the keys you input here are in CAPITALS, and space as ' '
    def pressKey(self, key):
        # Can only accept single character length values
        if (key.len() != 1):
            return
        self.win.SendMessage(win32con.WM_KEYDOWN, ord(key))

    # Moved the camera by x, y pixels relative to the center of the screen
    def moveMouseRelational(self, x, y):
        self.win.SendMessage(win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(self.basePosition["x"] + x, self.basePosition["y"] + y))

    # Move the camera by moving the mouse to the specified x, y coordinates 
    def moveMouseAbsolute(self, x, y):
        self.win.SendMessage(win32con.WM_MOUSEMOVE, 0, win32api.MAKELONG(x, y))


