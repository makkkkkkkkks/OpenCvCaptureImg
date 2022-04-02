from ctypes import windll
from datetime import datetime
from typing import Final

import cv2
import numpy as np
import pyautogui

import detect_mouse_position as dt


def saveOnClick(event):
    user32 = windll.user32
    user32.SetProcessDPIAware()
    name: Final = "C:/Users/m-rachipa/Downloads/img/" + datetime.utcnow().strftime('%Y-%m-%d_%H_%M_%S_%f')[
                                                        :-3] + "_pic.png"
    px = dt.getMousePosition()
    y = px[0]
    x = px[1]
    image = pyautogui.screenshot(region=(x, y, 400, 400))
    image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    cv2.imshow('Screenshot', np.array(image))
    cv2.imwrite(name, image)
    if event == 1:
        cv2.destroyAllWindows()
