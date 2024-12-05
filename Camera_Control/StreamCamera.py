import cv2


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret == False:
        break

    cv2.imshow("Camera Frame", frame)
    cv2.waitKey(1)

cap.release()
