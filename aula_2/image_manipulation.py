
import cv2


#convertendo a imagem em cinza
img = cv2.imread(r'C:\Users\harlo\Desktop\computacao_grafica\aula_2\farol.jpg')
imgCinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
print(f'RGB {img.shape}')
print(f'GRAY {imgCinza}')
cv2.imshow('Farol RGB', img)
cv2.imshow('Farol Cinza', imgCinza)
cv2.waitKey(0)