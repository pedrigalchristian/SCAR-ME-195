""" Displays the centroid of metallic object in bright lighting
conditions."""

import time
import numpy as np
from collections import deque

import cv2

import imutils


# Global Variables
sw = 1

# Camera Initializations
camera = cv2.VideoCapture(0)
if not camera.isOpened():
    raise Exception("Camera not detected.")

def nothing(x):
    pass
    
# Create Sliders
cv2.namedWindow("HSV", cv2.WINDOW_NORMAL)
cv2.createTrackbar("LH", "HSV", 0, 360, nothing)
cv2.createTrackbar("UH", "HSV", 360, 360, nothing)

cv2.createTrackbar("LS", "HSV", 0, 100, nothing)
cv2.createTrackbar("US", "HSV", 55, 100, nothing)

cv2.createTrackbar("LV", "HSV", 45, 100, nothing)
cv2.createTrackbar("UV", "HSV", 55, 100, nothing)

#cv2.createTrackbar("LS", "HSV", 0, 100, nothing)
#cv2.createTrackbar("US", "HSV", 75, 100, nothing)

#cv2.createTrackbar("LV", "HSV", 45, 100, nothing)
#cv2.createTrackbar("UV", "HSV", 60, 100, nothing)


# Main setup
time.sleep(2.0)

# Main Program
if __name__ == "__main__":
	while True:
		# Read a single frame and return exit flag
		flag, pic = camera.read()
		
		# Resize picture to 600p width while preserving aspect ratio
		pic = imutils.resize(pic, width = 600)
		
		# Convert pic into HSV color space
		blurred = cv2.GaussianBlur(pic,
								(11,11),
								 cv2.BORDER_DEFAULT
								)
		hsv_pic = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

		# Determine HSV values with Sliders
		l_h = cv2.getTrackbarPos("LH", "HSV")
		u_h = cv2.getTrackbarPos("UH", "HSV")
		
		l_h = np.round( l_h * (255/360))
		u_h = np.round( u_h * (255/360))
		
		l_s = cv2.getTrackbarPos("LS", "HSV")
		u_s = cv2.getTrackbarPos("US", "HSV")
		
		l_s = np.round( l_s * (255/100))
		u_s = np.round( u_s * (255/100))
		
		l_v = cv2.getTrackbarPos("LV", "HSV")
		u_v = cv2.getTrackbarPos("UV", "HSV")

		l_v = np.round( l_v * (255/100))
		u_v = np.round( u_v * (255/100))

		# Create mask
		l_b = np.array([l_h, l_s, l_v])
		u_b = np.array([u_h, u_s, u_v])
		mask = cv2.inRange(hsv_pic, l_b, u_b)

		# Get rid of noise using
		# Guassian Blur (making image blurry)
		# Eroding (Surrounding edges become darker)
		# Dilating (Make anything that light even lighter)
		denoise_mask = cv2.erode(mask, None, iterations = 2)
		denoise_mask = cv2.dilate(denoise_mask, None, iterations = 2)
		
		# edges = imutils.auto_canny(denoise_mask)
	
	
		# cv2.imshow('Edges', edges)
		
		denoise_mask = denoise_mask.astype(np.uint8)
		
		contour_count = cv2.findContours(denoise_mask.copy(),
										cv2.RETR_EXTERNAL,
										cv2.CHAIN_APPROX_SIMPLE
										)
		contour_count = imutils.grab_contours(contour_count)
		center = None
		


		if len(contour_count) > 0:
			c = max(contour_count, key = cv2.contourArea)
			if sw == 1:
				(last_xr, last_yr, last_wr, last_hr) = cv2.boundingRect(c)
				sw = 0
			(xr, yr, wr, hr) = cv2.boundingRect(c)
			
			
			# Complimentary Filter
			alpha = 0.6
			if last_xr != None:
				xr = int(alpha*xr + (1 - alpha)*last_xr)
				yr = int(alpha*yr + (1 - alpha)*last_yr)
				wr = int(alpha*wr + (1 - alpha)*last_wr)
				hr = int(alpha*hr + (1 - alpha)*last_hr)
			
			cv2.rectangle(pic,
						 (xr, yr),
						 (xr + wr, yr + hr),
						 (0, 0, 255),
						 2
						  )
						  
			#((x,y), radius) = cv2.minEnclosingCircle(c)
			#M = cv2.moments(c)
			#center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			#cv2.circle(pic, (int(x), int(y)), int(radius), 
			#(0, 255, 255), 2)
			#cv2.circle(pic, center, 5, (0, 0, 255, -1))
			
			pic = cv2.putText(pic, 
							'Mayo Scissors',
							 (xr, yr), # origin
							 cv2.FONT_HERSHEY_SIMPLEX, # font
							 1, # fontscale
							 (0, 0, 255), # color
							 2, # thickmess
							 cv2.LINE_AA # line type (optional)
							 )
							 
			(last_xr, last_yr, last_wr, last_hr) = (xr, yr, wr, hr)
								
		
		# cv2.imshow('Canny Edges', edges)
		cv2.imshow('Mask', mask)
		cv2.imshow('HSV', hsv_pic)
		cv2.imshow('FINAL', pic)

		key = cv2.waitKey(1)

		if key & 0xFF == ord('q'):
			cv2.destroyAllWindows()
			camera.release()
			break




