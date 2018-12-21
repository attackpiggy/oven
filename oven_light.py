import os
import numpy as np
import cv2
import tkinter


def main():
    img = cv2.imread(
        "C:\\Users\\attackpiggy\\Desktop\\oven_projects\\oven\\rsz_oven_on.jpg")
    # img=cv2.imread(
    #     "C:\\Users\\attackpiggy\\Desktop\\oven_projects\\oven\\oven_on.jpg")

    # cv2.namedWindow('img', cv2.WINDOW_NORMAL)
    # imS = cv2.resize(img, (960, 540))
    # blurring image
    median = cv2.medianBlur(img, 9)

    cv2.imshow('IMAGE', median)

    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'):  # wait for 's' key to save and exit

        cv2.imwrite('oven_onigray.png', img)
        cv2.destroyAllWindows()

        # now to blur the image


if __name__ == "__main__":
    main()
