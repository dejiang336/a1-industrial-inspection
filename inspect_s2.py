import cv2
img = cv2.imread("data/raw/raw_01.jpg")
if img is not None:
    print("读取成功,img.shape:", img.shape)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    print("gray.shape:", gray.shape)
    ret, binary = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    print("ret:", ret)
    print("binary.shape:", binary.shape)
    print(cv2.countNonZero(binary))
    cv2.imwrite("s2_bin.png", binary)
else:
    print("读取失败")