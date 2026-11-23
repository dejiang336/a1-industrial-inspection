#raw_02 和 raw_03 的区域数大概100和110
#阈值 100 → 150, 预测变小，基于raw_01做的判断
import os
import cv2

names = os.listdir("data/light_check")
for file in names:
    path = os.path.join("data/light_check", file)
    img = cv2.imread(path)
    if img is not None:
        img = cv2.resize(img, (960, 1280))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("文件名:", file, "区域数:", len(contours))
    else:
        print("读取失败,path:", path)
