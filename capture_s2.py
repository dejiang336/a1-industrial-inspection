import os
import cv2
import time

try:
    base_p = os.path.abspath("data/raw")
    t1 = time.time()
    cap = cv2.VideoCapture(0)
    os.makedirs(base_p, exist_ok = True)
    c = 1
    last_path = None
    while True:
        ret, frame = cap.read()
        cv2.imshow('v', frame)
        key = cv2.waitKey(1)
        t2 = time.time()
        x = t2 - t1
        filename = f"{"raw"}_{c:02d}{".jpg"}"
        path = os.path.join(base_p, filename)
        if key == ord(' '):
            if cv2.imwrite(path, frame):
                c += 1
                last_path = path
        if key == 27 or 30 - x <= 0:
            if last_path is not None:
                img = cv2.imread(last_path)
                print(img.shape)
            break
finally:
    cap.release()
    cv2.destroyAllWindows()

