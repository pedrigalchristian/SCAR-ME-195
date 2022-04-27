import cv2

# Open the device at the ID 0
cap = cv2.VideoCapture(0)

#Check whether used camerfa isopened successfully
if not (cap.isOpened()):
	print("Could not open video device")

if __name__ == "__main__":
	while True:
		flag, frame = cap.read()
		
		cv2.imshow('Camera', frame)
		 

		if cv2.waitKey(1) & 0xFF == ord('q'):
			cap.release()
			cv2.destroyAllWindows()
			break
        
