import cv2
import os

names = os.listdir("data/light_check")
for file in names:
    path = os.path.join("data/light_check", file)
    img = cv2.imread(path)
    if img is not None:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask = gray >= 250
        mask2 = gray <= 5
        ratio = mask.sum() / gray.size
        ratio2 = mask2.sum() / gray.size
        print('文件名：', file, '过曝比例：', ratio, '失曝比例：', ratio2, '均值：', gray.mean())
    else:
        print("读取失败")