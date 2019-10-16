import cv2 as cv
cap = cv.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    edges = cv.Canny(frame, 100, 110)
    cv.imshow('EdgeDisplay', edges)
    if cv.waitKey(1) == ord('q'):
        break
cap.release()
cv.destroyAllWindows()