import cv2
img = cv2.imread("data/raw/raw_01.jpg")
if img is not None:
    print(img.shape)
else:
    print("读取失败")