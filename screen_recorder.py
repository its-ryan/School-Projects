import cv2
import numpy as np
import pyautogui

screen_size=(1920,1080)
fourcc=cv2.VideoWriter_fourcc(*"XVID")
out=cv2.VideoWriter("output.avi",fourcc,20.0,(screen_size))
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Live", 480, 270)

while True:
    img=pyautogui.screenshot()
    frame=np.array(img)
    frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    out.write(frame)
    cv2.imshow("show",frame)
    if cv2.waitKey(1)==ord("q"):
        break

cv2.destroyAllWindows()
out.release()
