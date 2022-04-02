import time

from pynput.mouse import Button

previous_left = 0


def check_double_click(x, y, button, pressed):
    global previous_left
    if pressed and button == Button.left:
        current_left = time.time()
        diff_left = current_left - previous_left
        print('diff left:', diff_left)
        if diff_left < 0.7:
            print('double click left')
            return True
        previous_left = current_left
