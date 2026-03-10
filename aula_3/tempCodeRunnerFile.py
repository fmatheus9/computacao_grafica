import cv2

piramide = cv2.imread(r'C:\Users\harlo\Desktop\computacao_grafica\aula_3\piramide.jpg')

#transformando para a escala de cinza
piramideCinza = cv2.cvtColor(piramide, cv2.COLOR_RGB2GRAY)
piramideCinza = cv2.resize(piramideCinza, (500,400))

#desfoque gaussiano
piramideBlur = cv2.GaussianBlur(piramideCinza, (7,7), 0)

cv2.imshow('Piramide Original', piramide)
cv2.imshow('Piramide Cinza',piramideCinza)
cv2.imshow('Piramide Blur', piramideBlur)
cv2.waitKey(0)