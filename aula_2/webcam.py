import cv2

camera = cv2.VideoCapture(0)

while True:
    check, img = camera.read()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Webcam', img)
    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break 