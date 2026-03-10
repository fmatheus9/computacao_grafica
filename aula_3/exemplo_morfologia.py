import cv2

piramide = cv2.imread(r'C:\Users\harlo\Desktop\computacao_grafica\aula_3\piramide.jpg')

#transformando para a escala de cinza
piramideCinza = cv2.cvtColor(piramide, cv2.COLOR_RGB2GRAY)
piramideCinza = cv2.resize(piramideCinza, (500,400))

#desfoque gaussiano
piramideBlur = cv2.GaussianBlur(piramideCinza, (7,7), 0)

#canny edge
piramideCannyOG = cv2.Canny(piramide, 50, 100)
piramideCannyCZ = cv2.Canny(piramideCinza, 50, 100)
piramideCannyBL = cv2.Canny(piramideBlur, 50, 100)

#Dilatação
piramideDilate = cv2.dilate(piramideCannyOG, (5,5), iterations=5)

#Erosão
piramideErode = cv2.erode(piramideCannyOG, (5,5), iterations=5)

#Show
cv2.imshow('Piramide Original', piramide)
cv2.imshow('Piramide Cinza',piramideCinza)
cv2.imshow('Piramide Blur', piramideBlur)
cv2.imshow('Piramide Canny OG', piramideCannyOG)
cv2.imshow('Piramide Canny Cinza', piramideCannyCZ)
cv2.imshow('Piramide Canny Blur', piramideCannyBL)
cv2.imshow('Piramide Dilatada', piramideDilate)
cv2.imshow('Piramide Erosao', piramideErode)
cv2.waitKey(0)