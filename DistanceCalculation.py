import cv2
import numpy as np

def nothing(x):
    pass
##Camera
# create trackbars for color change

cv2.namedWindow('image1')
cv2.createTrackbar('RL','image1',0,255,nothing)
cv2.createTrackbar('RH','image1',255,255,nothing)
cv2.createTrackbar('GL','image1',0,255,nothing)
cv2.createTrackbar('GH','image1',255,255,nothing)
cv2.createTrackbar('BL','image1',0,255,nothing)
cv2.createTrackbar('BH','image1',255,255,nothing)
cap=cv2.VideoCapture(0)

ret,img=cap.read()
cv2.imshow('image',img)
(h, w) = img.shape[:2]
cv2.circle(img, (w//2, h//2), 7, (255, 255, 255), -1)
print("Frame Centroid is:")
print(w//2,h//2)
while(1):
    ret,img=cap.read()
    blurImg = cv2.blur(img,(10,10))
    rl = cv2.getTrackbarPos('RL','image1')
    rh = cv2.getTrackbarPos('RH','image1')
    gl = cv2.getTrackbarPos('GL','image1')
    gh = cv2.getTrackbarPos('GH','image1')
    bl = cv2.getTrackbarPos('BL','image1')
    bh = cv2.getTrackbarPos('BH','image1')
    lowerlimit=np.array([rl,gl,bl])
    higherlimit=np.array([rh,gh,bh])
    hsv=cv2.cvtColor(blurImg,cv2.COLOR_BGR2HSV)
    img_mask=cv2.inRange(hsv,lowerlimit,higherlimit)
    ##retval, threshold = cv2.threshold(img, 100,200,30,cv2.THRESH_BINARY)
    contours, _= cv2.findContours(img_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(blurImg,contours,-1,(0,255,0),3)
    cnt=contours[0]
    max_length=len(contours)
    for c in contours:
        if(len(c)>max_length):
            max_length=len(c)
            cnt=c
    
    
    M =cv2.moments(cnt)
    if (M["m00"]==0):
        M["m00"]=1
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    
    
    cv2.circle(blurImg,(cX,cY),8,(0,0,255),-1)
    r=cX-w//2
    p=cY-h//2
    if p==0:
       p=1
    if r==0:
        r=1
    
    angle=np.arctan(p/r)
    cv2.putText(blurImg,"Centroid:",(cX-25,cY-25),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,0,0),2)
    
    print("Distance is ",r,p)
    
    print("Angle is :",57.2957795*angle)
    
    
    # Taking a matrix of size 5 as the kernel 
    kernel = np.ones((5,5), np.uint8)
    # Divides image into matrices of 5X5 of 8 bits
    # The first parameter is the original image, 
    # kernel is the matrix with which image is  
    # convolved and third parameter is the number  
    # of iterations, which will determine how much  
    # you want to erode/dilate a given image.  
    img_mask = cv2.erode(img_mask, kernel, iterations=1) 
    img_mask = cv2.dilate(img_mask, kernel, iterations=1)
    cv2.imshow('Image',img)
    cv2.imshow('blurred image',blurImg)
    cv2.imshow('image2',img_mask)
    
    
    
    
    if cv2.waitKey(1)==27:          #if esc key is pressed then break out of loop
        break;
cv2.destroyAllWindows()
#Close and exit
##cap.release()   #releases the camera
##cv2.waitKey(5000)       #waits for program termination . If 0 then waits infinetely for user input


