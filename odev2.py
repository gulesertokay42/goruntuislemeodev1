import cv2
import numpy as np

cap = cv2.VideoCapture(0)  # Kamera başlat

while True:
    ret, frame = cap.read()   # Kamerayı okuma

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Görüntüyü HSV ye dönüştürür

    lower_red = np.array([0, 100, 100])   # Kırmızı rengin  HSV aralığını belirleme
    upper_red = np.array([10, 255, 255])

    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)  # Kırmızı renk için maske oluşturur
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)   # Kırmızı nesneyi gösterir, diğerlerini gizler

    cv2.imshow('Normall Görüntü', frame)     # Görüntüleri gösterir
    cv2.imshow('Sadece Kirmizi Nesne', red_result)

    if cv2.waitKey(1) == ord('e'):  # e ye tıklayınca çıkış yapar
        break

cap.release()
cv2.destroyAllWindows()