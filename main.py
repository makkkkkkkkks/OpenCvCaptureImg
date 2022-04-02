import datetime
import sys
import time
from typing import Final

import cv2
import mss
from pynput import keyboard
from pynput import mouse
from pynput.keyboard import Listener as KeyboardListener
from pynput.mouse import Listener as MouseListener

import detect_mouse_position as dt


def on_release(key):
    print("Key released: {0}".format(key))
    if key == keyboard.Key.f8:
        keyboard_listener.stop()
        mouse_listener.stop()
        sys.exit()


def on_click(x, y, button, pressed):
    if pressed and button == mouse.Button.left:
        saveOnClick2()

    if pressed and button == mouse.Button.right:
        cv2.destroyAllWindows()
        quit()
        sys.exit()


def saveOnClick2():
    ts = time.time()
    st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')

    name = str(st) + "_pic.png"
    path: Final = "C:/Users/m-rachipa/Downloads/img/" + name
    px = dt.getMousePosition()
    y = px[0] - 200
    x = px[1] - 200
    monitor = {"top": x, "left": y, "width": 400, "height": 400}

    # Grab the data
    sct_img = mss.mss().grab(monitor)
    # Save to the picture file
    mss.tools.to_png(sct_img.rgb, sct_img.size, output=path)

    return sct_img


# Setup the listener threads
keyboard_listener = KeyboardListener(on_release=on_release)
mouse_listener = MouseListener(on_click=on_click)

# Start the threads and join them so the script doesn't end early
keyboard_listener.start()
mouse_listener.start()
keyboard_listener.join()
mouse_listener.join()
