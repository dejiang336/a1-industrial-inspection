import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
cv2.imshow('cap', frame)
cv2.waitKey(0)
cap.release()
cv2.destroyAllWindows()