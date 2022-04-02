# import datetime
# import time
# from typing import Final
#
# import cv2
# import mss
# import numpy
#
# import detect_mouse_position as dt
#
#
# def saveOnClick2():
#     ts = time.time()
#     st = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d-%H-%M-%S')
#
#     name = str(st) + "_pic.png"
#     path: Final = "C:/Users/m-rachipa/Downloads/img/" + name
#     px = dt.getMousePosition()
#     y = px[0] - 200
#     x = px[1] - 200
#     monitor = {"top": x, "left": y, "width": 400, "height": 400}
#
#     # Grab the data
#     sct_img = mss.mss().grab(monitor)
#
#     img = numpy.array(sct_img)
#
#     cv2.imshow(name, img)
#     # Save to the picture file
#     mss.tools.to_png(sct_img.rgb, sct_img.size, output=path)
#
#
#     return  sct_img
#     # Press "q" to quit
#     if cv2.waitKey(25) & 0xFF == ord("q"):
#         cv2.destroyAllWindows()
#
# print(saveOnClick2())