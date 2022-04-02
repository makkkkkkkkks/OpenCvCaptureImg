from pynput.mouse import Controller


def getMousePosition():
    mouse = Controller()
    current_mouse_position = mouse.position
    return current_mouse_position
