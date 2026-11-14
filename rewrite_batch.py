import os
import cv2

names = os.listdir("data/raw")
for name in names:
    path = os.path.join("data/raw", name)
    img = cv2.imread(path)
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        counters, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("文件:", name, "区域数:", len(counters))
    else:
        print("读取失败, path:", path)