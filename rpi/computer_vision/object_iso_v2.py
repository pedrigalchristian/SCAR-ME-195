import cv2
import numpy as np


# Global Variables
WINDOW_NAME = 'Scissors'


# Camera Initialization
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise Exception("Camera not detected.")


def nothing(x):
    pass

# Create Sliders
cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
cv2.createTrackbar("LH", "HSV", 0, 255, nothing)
cv2.createTrackbar("UH", "HSV", 255, 255, nothing)

cv2.createTrackbar("LS", "HSV", 0, 255, nothing)
cv2.createTrackbar("US", "HSV", 255, 255, nothing)

cv2.createTrackbar("LV", "HSV", 0, 255, nothing)
cv2.createTrackbar("UV", "HSV", 255, 255, nothing)

cv2.namedWindow("Cropping", cv2.WINDOW_NORMAL)
cv2.createTrackbar("X1", "Cropping", 0, 1280, nothing)
cv2.createTrackbar("X2", "Cropping", 1280, 1280, nothing)

cv2.createTrackbar("Y1", "Cropping", 0, 720, nothing)
cv2.createTrackbar("Y2", "Cropping", 720, 720,  nothing)


while True:
    flag, pic = camera.read()
    hsv_pic = cv2.cvtColor(pic, cv2.COLOR_BGR2HSV)


    # Determine HSV values with Sliders
    l_h = cv2.getTrackbarPos("LH", "HSV")
    u_h = cv2.getTrackbarPos("UH", "HSV")

    l_s = cv2.getTrackbarPos("LS", "HSV")
    u_s = cv2.getTrackbarPos("US", "HSV")

    l_v = cv2.getTrackbarPos("LV", "HSV")
    u_v = cv2.getTrackbarPos("UV", "HSV")


    # Create mask
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv_pic, l_b, u_b)


    # Bitwise operations with self using mask
    result = cv2.bitwise_and(pic, pic, mask = mask)
    # cv2.imshow('Result Scissors', result)
    
    # Create sliders for Cropping
    x1 = cv2.getTrackbarPos("X1", "Cropping")
    x2 = cv2.getTrackbarPos("X2", "Cropping")
    y1 = cv2.getTrackbarPos("Y1", "Cropping")
    y2 = cv2.getTrackbarPos("Y2", "Cropping")


    # Create Cropping Mask
    black_pic = np.zeros(pic.shape[:2], dtype = np.uint8)
    white_color = 255
    thickness = -1
    white_rect = cv2.rectangle(black_pic,
                                (x1, y1),
                                (x2, y2),
                                white_color,
                                 thickness
                                 )

    # Bitwise operations with first mask with second mask
    final_result = cv2.bitwise_and(result, result, mask = white_rect)
    cv2.imshow('Result Scissors', final_result)

    # Show results
    # cv2.imshow('Scissors', pic)
    # cv2.imshow('Mask', mask)

    key = cv2.waitKey(1)

    if key & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        camera.release()
        break
