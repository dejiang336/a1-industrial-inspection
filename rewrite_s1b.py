import cv2
import time

try:
    t1 = time.time()
    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        cv2.imshow('ve', frame)
        key = cv2.waitKey(1)
        t2 = time.time()
        x = t2 - t1
        if key == 27 or 30 - x <= 0:
            break
finally:
    cap.release()
    cv2.destroyAllWindows()

