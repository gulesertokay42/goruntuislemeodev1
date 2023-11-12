import cv2
import numpy as np
import matplotlib.pyplot as plt

resim = cv2.imread("python/goruntuisleme/hafta1/peppers.png")  # Görüntüyü siyah beyaz olarak okuyoruz
goruntu = cv2.cvtColor(resim, cv2.COLOR_BGR2GRAY)
cv2.imshow("peppers",goruntu)


def histogram_hesapla(goruntu):
    histogram = np.zeros(256)

    for i in range(goruntu.shape[0]):
        for j in range(goruntu.shape[1]):
            a = goruntu[j, i]
            histogram[a] += 1

    return histogram

histogram = histogram_hesapla(goruntu)

plt.plot(histogram, color='black')
plt.xlabel('Piksel Değerleri')
plt.ylabel('Piksel Sayısı')
plt.show()