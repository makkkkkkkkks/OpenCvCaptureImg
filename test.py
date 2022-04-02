from datetime import datetime

import cv2
import cv2 as cv
import numpy as np
import pyautogui
from typing import Final
from pynput.mouse import Listener
import pygame
import detect_mouse_position as dt


# mouse callback function
def draw_circle(event, x, y, flags, param):
    name: Final = "C:/Users/m-rachipa/Downloads" + datetime.utcnow().strftime('%Y-%m-%d_%H_%M_%S_%f')[:-3] + "_pic.png"
    if event == cv.EVENT_LBUTTONDBLCLK:
        px = dt.getMousePosition()
        y = px[0] - 200
        x = px[1] - 100
        image = pyautogui.screenshot(region=(x, y, 400, 400))
        image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        cv2.imshow('Screenshot', np.array(image))
        cv2.imwrite(name, image)
        print(name)


# Create a black image, a window and bind the function to window
img = np.zeros((512, 512, 3), np.uint8)
cv.namedWindow('image')
cv.setMouseCallback('image', draw_circle)
while (1):

    if pyautogui.click(button='left'):
        print("right")
    if cv.waitKey(20) & 0xFF == 27:
        break
cv.destroyAllWindows()
