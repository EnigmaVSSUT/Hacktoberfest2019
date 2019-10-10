import numpy as np
import cv2
from PIL import Image
#img = cv2.imread('shapes.jpg')

cap = cv2.VideoCapture(0)

while True:
	_,frame = cap.read()
	gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	gray = np.float32(gray)
	
	threshold_1 = 100
	threshold_2 = 200
	edge = cv2.Canny(frame,threshold_1,threshold_2)
	#cv2.imshow('Original',edge)



	corners = cv2.goodFeaturesToTrack(gray, 100, 0.001, 10)
	corners = np.int0(corners)

	
	for corner in corners:
	    x,y = corner.ravel()
	    cv2.circle(edge,(x,y),3,255,-1)
	    cv2.imshow('Corner',edge)

	
	    
	
	k=cv2.waitKey(5) & 0xFF	
	if k==27:
		break

cv2.destroyAllWindows()
cap.release()