import cv2
import numpy as np

img = cv2.imread('input.jpg') #Назначаем изображение
img = cv2.resize(img, (500, 500)) #Изменение размера
#img = cv2.GaussianBlur(img, (5,5), 0) #Размытие

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #Изменение цвета/слоёв

#img = cv2.Canny(img, 100, 100) #Создание углов

one = np.ones((4, 4)) #Создаём матрицу
img = cv2.dilate(img, one, iterations=2) #Обводка

cv2.imshow('Cat', img) #Показываем изображение с именем

print(img.shape) #разрешение + слои
cv2.waitKey(0) #Время которое будет открыта картинка. 0 - всегда