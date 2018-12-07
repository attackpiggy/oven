import os
import numpy as np
import cv2


def main():
    img = cv2.imread('oven_on.jpg',1)
    cv2.imshow('image',img)
    final_pic=cv2.medianBlur(img,9)
    cv2.imshow('image',final_pic)
    
    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'): # wait for 's' key to save and exit
        cv2.imwrite('oven_onigray.png',img)
        cv2.destroyAllWindows()

     #now to blur the image 
       



if __name__ == "__main__":
    main()