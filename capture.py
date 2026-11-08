import time
import os
import cv2

def save_frame(frame, path):
    success = cv2.imwrite(path, frame)
    if not success:
        print(f"保存失败：{path}")
    else:
        print(f"保存成功：{path}")
    return success

def main():
    try:
        base_p = "data/raw"
        os.makedirs(base_p, exist_ok = True)
        cap = None
        cap = cv2.VideoCapture(0)
        t1 = time.time()
        c = 1
        last_path = None
        while True:
            ret, frame = cap.read()
            cv2.imshow('v', frame)
            filename = f"raw_{c:02d}.jpg"
            path = os.path.join(base_p, filename)
            key = cv2.waitKey(1)
            if (key &0XFF) == ord(' '):
                if save_frame(frame, path):
                    last_path = path
                    c += 1
            t2 = time.time()
            x = t2 - t1
            if (key &0XFF) == ord('q') or (key &0XFF) == 27 or 30 - x <= 0:
                if last_path is not None:
                    print(frame.shape)
                break
    finally:
        if cap is not None:
            cap.release()
        cv2.destroyAllWindows()
if __name__ == "__main__":
    main()