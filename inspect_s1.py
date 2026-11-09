# 预测：raw_01.jpg 的 shape = (640, 480)，因为 宽比高长，是横图，而且之前见过
# 实际上(480, 640, 3)
import cv2
img = cv2.imread("data/raw/raw_01.jpg")
if img is not None:
    print(img.shape)
else:
    print("读取失败")

