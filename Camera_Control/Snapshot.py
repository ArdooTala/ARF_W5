import cv2
from datetime import datetime

cap = cv2.VideoCapture(0)

try:
    while True:
        ret, frame = cap.read()
        if ret == False:
            break

        cv2.imshow("Camera Frame", frame)
        
        key_pressed = cv2.waitKey(1)

        if key_pressed == ord(' '):
            t = datetime.now().strftime("%Y%m%d-%H%M%S")
            cv2.imwrite(f"IMG_{t}.png", frame)
        
        if key_pressed == ord('q'):
            break

finally:
    cap.release()
