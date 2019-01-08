import os
import numpy as np
import cv2
import tkinter


def create_hue_mask(image, lower_color, upper_color):
    lower = np.array(lower_color, np.uint8)
    upper = np.array(upper_color, np.uint8)

    # Create a mask from the colors
    mask = cv2.inRange(image, lower, upper)
    output_image = cv2.bitwise_and(image, image, mask=mask)
    return output_image


def main():
    img = cv2.imread(
        "C:\\Users\\attackpiggy\\Desktop\\oven_projects\\oven\\rsz_oven_on.jpg")
    # img=cv2.imread(
    #     "C:\\Users\\attackpiggy\\Desktop\\oven_projects\\oven\\oven_on.jpg")

    # blurring image
    median = cv2.medianBlur(img, 9)

    cv2.imwrite('image_blurred.png', median)

    # coverting images to hsv

    hsv_image = cv2.cvtColor(median, cv2.COLOR_BGR2HSV)
    cv2.imwrite('HSV_IMAGES.png', hsv_image)

    # now getting lower and higher hue for seperation

    lower_red_hue = create_hue_mask(hsv_image, [0, 100, 100], [10, 255, 255])
    cv2.imwrite('lower_red_hue.png', lower_red_hue)
    higher_red_hue = create_hue_mask(
        hsv_image, [160, 100, 100], [179, 255, 255])

    # connecting the lower and higher hue images and putting it together
    whole_image = cv2.addWeighted(lower_red_hue, 1.0, higher_red_hue, 1.0, 0.0)

    cv2.imwrite('higher_red_hue.png', higher_red_hue)

    cv2.imshow('IMAGE', lower_red_hue)

    cv2.imshow('IMAGE', higher_red_hue)

    k = cv2.waitKey(0)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
    elif k == ord('s'):  # wait for 's' key to save and exit

        cv2.imwrite('1oven_onigray.png', hsv_image)
        cv2.imwrite('2oven_onigray.png', lower_red_hue)
        cv2.imwrite('3oven_onigray.png', higher_red_hue)

        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
