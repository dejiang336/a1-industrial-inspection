# 预测（2026-11-25）
# 1) 三张图的 Otsu 阈值 ret 各不相同；L11 的 ret 落在 100~239 之间（油墨与纸面之间）——因为阈值是按每张图自己的直方图算的；判据：打印的 ret，和 L11 油墨 58-100、纸面 239-249 这两段比。
# 2) 区域数：L37/L61 仍然崩（≈1，跟阈值 100/150 时一样）——因为油墨-纸面只差 5-10 级，ret 落哪边都切不干净；判据：区域数和 1 比。
# 3) L11 的区域数本轮不判好坏——因为没裁 ROI，Day 14 已证 155 主要是画面左下杂物；判据：本轮只看 L11 的 ret 落点，不看它的区域数。

import os
import cv2

names = [f for f in os.listdir("data/light_check") if f.lower().endswith('.jpg')]
for file in names:
    path = os.path.join("data/light_check", file)
    img = cv2.imread(path)
    if img is not None:
        img = cv2.resize(img, (960, 1280))
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        contours, hierarchy = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        print("文件名:", file, "区域数:", len(contours), "阈值:", ret)
    else:
        print("读取失败,path:", path)
