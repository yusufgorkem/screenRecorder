import cv2
import numpy as np
import pyautogui
import time

SCREEN_SIZE = (1920, 1080)

fourcc = cv2.VideoWriter.fourcc(*"XVID")
out = cv2.VideoWriter("recordings/new_record.avi", fourcc, 20.0, SCREEN_SIZE)

fps = 120
prev = 0

while True:
    try:
        time_elapsed = time.time() - prev
        img = pyautogui.screenshot()
        if time_elapsed > 1.0 / fps:
            prev = time.time()
            frame = np.array(img)
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            out.write(frame)
            cv2.waitKey(100)
    except KeyboardInterrupt:
        break

cv2.destroyAllWindows()
out.release()
