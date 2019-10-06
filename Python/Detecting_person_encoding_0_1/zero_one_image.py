import numpy as np
import cv2
import random

def nothing(x):
    pass

cap = cv2.VideoCapture(1)
ret, frame = cap.read()
height, width, channels = frame.shape
frame = cv2.resize(frame, (int(width * 1.5),int(height * 1.5)), interpolation = cv2.INTER_AREA)
height, width, channels = frame.shape


img = np.zeros((height, width, channels), np.uint8)
val = np.zeros((height, width, 2), np.int)
for x in range( 0,(width-1),6):
    for y in range(0,(height-1),12):
        val[y][x][0]=random.randrange(2)
        val[y][x][1]=val[y][x][0]
        #cv2.putText(img, str(val[y][x]), (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
            
cv2.namedWindow('image')

cv2.createTrackbar('H_high','image',255,255,nothing)
cv2.createTrackbar('H_low','image',0,255,nothing)
cv2.createTrackbar('S_high','image',255,255,nothing)
cv2.createTrackbar('S_low','image',0,255,nothing)
cv2.createTrackbar('V_high','image',255,255,nothing)
cv2.createTrackbar('V_low','image',0,255,nothing)

while(True):
    img = np.zeros((height, width, channels), np.uint8)
    ret, frame = cap.read()
    height, width, channels = frame.shape
    frame = cv2.resize(frame, (int(width * 1.5),int(height * 1.5)), interpolation = cv2.INTER_AREA)
    height, width, channels = frame.shape

    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    H_high = cv2.getTrackbarPos('H_high','image')
    H_low = cv2.getTrackbarPos('H_low','image')
    S_high = cv2.getTrackbarPos('S_high','image')
    S_low = cv2.getTrackbarPos('S_low','image')
    V_high = cv2.getTrackbarPos('V_high','image')
    V_low = cv2.getTrackbarPos('V_low','image')

    kernel = np.ones((5,5), np.uint8) 

    mask = cv2.inRange(HSV, (H_low,S_low,V_low), (H_high,S_high,V_high))
     
    mask = cv2.dilate(mask, kernel, iterations=1)
    mask = cv2.erode(mask, kernel, iterations=1)
    for x in range( 0,(width-1),10):
        val[0][x][0] = random.randrange(2)

    for x in range( 0,(width-1),10):
        for y in range(0,(height-1),15):
            val[y][x][1]=val[y][x][0]
            val[y][x][0] = val[y-12][x][1]
            #if(mask[y][x] == 0):
            cv2.putText(img, str(val[y][x][0]), (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (67, 204, 52), 1, cv2.LINE_AA)
            #else:
                #cv2.putText(img, ' ', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
            #x=x+5
            #y=y+5
    #print(mask[300][300])
    img = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow("imag", mask)
    cv2.imshow("Result", img)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    img = np.zeros((height, width, channels), np.uint8)
    for x in range( 0,(width-1),10):
        for y in range(0,(height-1),15):
            val[y][x][1]=val[y][x][0]
            val[y][x][0] = val[y-12][x][1]
            #if(mask[y][x] == 0):
            cv2.putText(img, str(val[y][x][0]), (x, y + 5),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (67, 204, 52), 1, cv2.LINE_AA)
            #else:
                #cv2.putText(img, ' ', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
            #x=x+5
            #y=y+5
    #print(mask[300][300])
    img = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow("imag", mask)
    cv2.imshow("Result", img)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    img = np.zeros((height, width, channels), np.uint8)
    for x in range( 0,(width-1),10):
        for y in range(0,(height-1),15):
            val[y][x][1]=val[y][x][0]
            val[y][x][0] = val[y-12][x][1]
            #if(mask[y][x] == 0):
            cv2.putText(img, str(val[y][x][0]), (x, y + 10),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (67, 204, 52), 1, cv2.LINE_AA)
            #else:
                #cv2.putText(img, ' ', (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 255, 0), 1, cv2.LINE_AA)
            #x=x+5
            #y=y+5
    #print(mask[300][300])
    img = cv2.bitwise_and(img,img, mask= mask)
    cv2.imshow("imag", mask)
    cv2.imshow("Result", img)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
exit(0)
