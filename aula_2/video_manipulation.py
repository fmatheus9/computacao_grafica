import cv2

video = cv2.VideoCapture(r'C:\Users\harlo\Desktop\computacao_grafica\aula_2\runners.mp4')
while True:
    check, img = video.read()
    cv2.imshow('Video', img)
    imgRedim = cv2.resize(img, (640,420))
    cv2.waitKey(10)