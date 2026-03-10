import cv2

piramide = cv2.imread(r'aula_3/piramide.jpg')
piramide = cv2.resize(piramide, (600,400))

#colocando formas
cv2.rectangle(piramide, (50,50), (200,200), (255,0,0), -2)
cv2.circle(piramide, (300,300), (200), (0,255,0), 2)

cv2.imshow('Piramide', piramide)
cv2.waitKey(0)
