import cv2

img = cv2.imread('data/calib/calib_20261122_1-40_mf_01.jpg')
if img is not None:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = gray >= 250
    mask2 = gray <= 5
    ratio = mask.sum() / gray.size
    ratio2 = mask2.sum() / gray.size
    print(ratio)
    print(ratio2)
else:
    print("读取失败")