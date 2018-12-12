# -*- coding: utf-8 -*-
"""
Created on Mon Dec 10 21:56:49 2018

@author: pc
"""


def main():
    print("welcome to the image calculator!")
    try:
        camerachooose=int(input("if you use Local camera,please enter 0 ; if you use usb camera , please enter freedowm number:"))
    except:
        print("input error")
    import cv2
    cam_input =cv2.VideoCapture(cameranumber) 
    while True:
        ret, frame = cam_input.read()
        cv2.imshow("Imsthage", frame) 
    if cv2.waitKey(1) & 0xFF == ord('1'):
          cv2.imwrite("image.jpeg", frame)
          break
    cam_input.release()
    cv2.destroyAllWindows()  


main()
