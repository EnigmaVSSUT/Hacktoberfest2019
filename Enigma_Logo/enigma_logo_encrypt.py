import numpy as np 
import cv2
import random
 
img = cv2.imread('enigma_logo@3.png', cv2.IMREAD_UNCHANGED)
height, width, a = img.shape
#print(img.shape)
#img = cv2.resize(img, (int(width * .6),int(height * .6)), interpolation = cv2.INTER_AREA)
#height, width, a = img.shape

frame_height = 830
frame_width = 1580
frame = np.zeros((frame_height, frame_width, 4), np.uint8)
val = np.zeros((frame_height, frame_width, 2), np.int)
for x in range( 0,(frame_width-1),6):
    for y in range(0,(frame_height-1),12):
        val[y][x][0]=random.randrange(2)
        val[y][x][1]=val[y][x][0]

y_low = int((frame_width/2)-(width/2))
y_high = int((frame_width/2)+(width/2))
x_low = int((frame_height/2)-(height/2))
x_high = int((frame_height/2)+(height/2))
print(height,width)

for y in range(y_low, y_high):
    for x in range(x_low, x_high):
        if((x-x_low) < width and (y-y_low) < height):
            frame[x][y]=img[x - x_low][y - y_low]
            #if(img[x - x_low][y - y_low][0] != 0):
                #print(x,y,frame[x][y])

cv2.imwrite('enigma_logo_big.png',frame)

while(1):
    frame = cv2.imread('enigma_logo_big.png', cv2.IMREAD_UNCHANGED)
    for x in range( 0,(frame_width-1),10):
        val[0][x][0] = random.randrange(3)
    for x in range( 0,(frame_width-1),10):
        for y in range(0,(frame_height-1),15):
            val[y][x][1]=val[y][x][0]
            val[y][x][0] = val[y-15][x][1]
            X = x + 6
            Y = y + 3
            if(X < frame_width and Y < frame_height and frame[Y][X][0] == 0 and frame[y][x][0] == 0 and frame[y-3][x][0] == 0 and val[y][x][0] < 2):
                cv2.putText(frame, str(val[y][x][0]), (x, y),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (67, 204, 52), 1, cv2.LINE_AA)
            #if(X < frame_width and Y < frame_height and frame[Y][X][0] == 0 and frame[y][x][0] == 0 and frame[y-3][x][0] == 0 and val[y][x][0] == 3):
                #cv2.putText(frame, str(random.randrange(3)), (x, y+6),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 100, 0), 1, cv2.LINE_AA)

##    for y in range(y_low, y_high):
##        for x in range(x_low, x_high):
##            #frame[x][y][0] = 255
##            if((x-x_low) < width and (y-y_low) < height):
##                if(img[x - x_low][y - y_low][1] > 0):
##                    frame[x][y]=img[x - x_low][y - y_low]
                #else:
                    #print(img[x - x_low][y - y_low][0])

    cv2.line(frame, (y_low, x_low), (y_high, x_high), (67, 204, 52), 10)
    cv2.imshow('image', frame)

    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break
    
    frame = cv2.imread('enigma_logo_big.png', cv2.IMREAD_UNCHANGED)
    for x in range( 0,(frame_width-1),10):
        for y in range(0,(frame_height-1),15):
            X = x + 6
            Y = y + 3
            if(X < frame_width and Y < frame_height and frame[Y][X][0] == 0 and frame[y][x][0] == 0 and frame[y-3][x][0] == 0 and val[y][x][0] < 2):
                cv2.putText(frame, str(val[y][x][0]), (x, y+5),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (67, 204, 52), 1, cv2.LINE_AA)
            #if(X < frame_width and Y < frame_height and frame[Y][X][0] == 0 and frame[y][x][0] == 0 and frame[y-3][x][0] == 0 and val[y][x][0] == 3):
                #cv2.putText(frame, str(random.randrange(3)), (x, y+6),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 100, 0), 1, cv2.LINE_AA)

##    for y in range(y_low, y_high):
##        for x in range(x_low, x_high):
##            #frame[x][y][0] = 255
##            if((x-x_low) < width and (y-y_low) < height):
##                if(img[x - x_low][y - y_low][1] > 0):
##                    frame[x][y]=img[x - x_low][y - y_low]
    cv2.line(frame, (y_low, x_low), (y_high, x_high), (67, 204, 52), 10)
    cv2.imshow('image', frame)

    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break
    
    frame = cv2.imread('enigma_logo_big.png', cv2.IMREAD_UNCHANGED)
    for x in range( 0,(frame_width-1),10):
        for y in range(0,(frame_height-1),15):
            X = x + 6
            Y = y + 3
            if(X < frame_width and Y < frame_height and frame[Y][X][0] == 0 and frame[y][x][0] == 0 and frame[y-3][x][0] == 0 and val[y][x][0] < 2):
                cv2.putText(frame, str(val[y][x][0]), (x, y+10),cv2.FONT_HERSHEY_SIMPLEX, 0.4, (67, 204, 52), 1, cv2.LINE_AA)
            #if(X < frame_width and Y < frame_height and frame[Y][X][0] == 0 and frame[y][x][0] == 0 and frame[y-3][x][0] == 0 and val[y][x][0] == 3):
                #cv2.putText(frame, str(random.randrange(3)), (x, y+6),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 100, 0), 1, cv2.LINE_AA)

##    for y in range(y_low, y_high):
##        for x in range(x_low, x_high):
##            #frame[x][y][0] = 255
##            if((x-x_low) < width and (y-y_low) < height):
##                if(img[x - x_low][y - y_low][1] > 0):
##                    frame[x][y]=img[x - x_low][y - y_low]
    cv2.line(frame, (y_low, x_low), (y_high, x_high), (67, 204, 52), 10)
    cv2.imshow('image', frame)
    
    k = cv2.waitKey(1) & 0xFF
    
    if k == 27:
        break
    
cv2.destroyAllWindows()  
exit(0)
