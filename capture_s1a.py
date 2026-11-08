import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
print(frame.shape)
cv2.imshow("cap", frame)
# 我预测：改成 waitKey(1) 后，窗口会出现1毫秒，然后自己关闭，因为delay>0,会等delay毫秒
# 预测正确，实际现象符合预测
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()