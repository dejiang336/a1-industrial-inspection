import cv2
import time
import os

try:
    cap = None
    cap = cv2.VideoCapture(0)
    last_path = None
    x = 0
    t1 = time.time()
    base_p = os.path.abspath("data/raw")
    os.makedirs(base_p, exist_ok = True)
    c = 1
    while True:
        ret, frame = cap.read()
        t2 = time.time()
        x = t2 - t1
        cv2.imshow('v', frame)
        key = cv2.waitKey(1)
        filename = f"raw_{c:02d}.jpg"
        path = os.path.join(base_p, filename)
        if key == ord(' '):
            cv2.imwrite(path, frame)
            last_path = path
            c += 1
        if (key &0xFF) == 27 or (key &0xFF) == ord('q') or 30 - x <= 0:
            if last_path is not None:
                print(frame.shape)
            break
finally:
    if cap is not None:
        cap.release()
    cv2.destroyAllWindows()
