import os
import cv2

names = [f for f in os.listdir("data/light_check") if f.lower().endswith(".jpg")]
for name in names:
    path = os.path.join("data/light_check", name)
    img = cv2.imread(path)
    if img is not None:
        img = cv2.resize(img, (960, 1280))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("文件名:", name, "区域数量:", len(contours))
    else:
        print("读取失败")