import cv2
import glob
import os
import numpy as np
def playback():
    cap = cv2.VideoCapture(r'data/sample.mov')
    if (cap.isOpened()== False):  
        print("ビデオファイルを開くとエラーが発生しました")
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            cv2.imshow("Video", frame)
            if cv2.waitKey(25) & 0xFF == ord('q'): 
                break
        else:
            break

    cap.release()
    cv2.destroyAllWindows()

playback() #再生
