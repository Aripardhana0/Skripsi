import cv2
import numpy as np
from pygame import mixer
import serial
from time import sleep

ser = serial.Serial("COM1", 9600)
b   = 0
bb  = 0
bg  = 0
by  = 0
b2  = 0
cap = cv2.VideoCapture(0)
mixer.init()

while True:
    _, image = cap.read()
    #image = cv2.imread("rgb.png")
    pengali = 1
    x = image.shape[1] * pengali
    y = image.shape[0] * pengali
    dimensi = (x,y)
    resize  = cv2.resize(image,dimensi)
    result  = resize.copy()

    resize2 = resize.copy()
    result2 = resize.copy()

    resize3 = resize.copy()
    result3 = resize.copy()

    resize4 = resize.copy()
    result4 = resize.copy()

    resize = cv2.cvtColor(resize, cv2.COLOR_BGR2HSV)
    resize2 = cv2.cvtColor(resize2, cv2.COLOR_BGR2HSV)
    resize3 = cv2.cvtColor(resize3, cv2.COLOR_BGR2HSV)
    resize4 = cv2.cvtColor(resize4, cv2.COLOR_BGR2HSV)

    #Range warna Putih
    lower_putih = np.array([0, 100, 100])
    upper_putih = np.array([10, 255, 255])
    mask_putih = cv2.inRange(resize, lower_putih, upper_putih)
    edge_putih = cv2.Canny(mask_putih,240,255)

    #Range warna Abu - Abu
    lower_abuabu = np.array([40, 40, 40])
    upper_abuabu = np.array([80, 255, 255]) 
    mask_abuabu = cv2.inRange(resize2, lower_abuabu, upper_abuabu)
    edge_abuabu = cv2.Canny(mask_abuabu,240,255)

    #Range warna Hitam
    lower_hitam = np.array([100, 100, 100])
    upper_hitam = np.array([130, 255, 255])
    mask_hitam = cv2.inRange(resize3, lower_hitam, upper_hitam)
    edge_hitam = cv2.Canny(mask_hitam,240,255)

    #Range warna Coklat
    lower_coklat = np.array([20, 100, 100])
    upper_coklat = np.array([40, 255, 255])
    mask_coklat = cv2.inRange(resize4, lower_coklat, upper_coklat)
    edge_coklat = cv2.Canny(mask_coklat,240,255)


    contours_putih , hierarchy = cv2.findContours(edge_putih,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours_abuabu , hierarchy2 = cv2.findContours(edge_abuabu,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours_hitam , hierarchy3 = cv2.findContours(edge_hitam,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours_coklat , hierarchy4 = cv2.findContours(edge_coklat,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


    jumlah_putih  = len(contours_putih)
    jumlah_abuabu = len(contours_abuabu)
    jumlah_hitam = len(contours_hitam)
    jumlah_coklat = len(contours_coklat)
 
    jumlahWarna : int
    jumlahWarna = ((jumlah_putih + jumlah_abuabu + jumlah_hitam + jumlah_coklat))
    
    if jumlah_putih != 0 and b == 0:
        if not mixer.music.get_busy():
            mixer.music.load("adaputih.mp3")
            mixer.music.play()
        else:
            sleep(2)
            mixer.music.load("adaputih.mp3")
            mixer.music.play()
        ser.write(b"r")
        print("Putih")
        b = 1

    if jumlah_putih <= 0 and b == 1:
        b = 0

    if jumlah_abuabu != 0 and bb == 0:
        if not mixer.music.get_busy():
            mixer.music.load("adaabuabu.mp3")
            mixer.music.play()
        else:
            sleep(2)
            mixer.music.load("adaabuabu.mp3")
            mixer.music.play()
        ser.write(b"b")
        print("Abu - Abu")
        bb = 1

    if jumlah_abuabu <= 0 and bb == 1:
        bb = 0

    if jumlah_hitam != 0 and bg == 0:
        if not mixer.music.get_busy():
            mixer.music.load("adahitam.mp3")
            mixer.music.play()
        else:
            sleep(2)
            mixer.music.load("adahitam.mp3")
            mixer.music.play()
        ser.write(b"g")
        print("Hitam")
        bg = 1

    if jumlah_hitam <= 0 and bg == 1:
        bg = 0

    if jumlah_coklat != 0 and by == 0:
        if not mixer.music.get_busy():
            mixer.music.load("adacoklat.mp3")
            mixer.music.play()
        else:
            sleep(2)
            mixer.music.load("adacoklat.mp3")
            mixer.music.play()
        ser.write(b"y")
        print("Coklat")
        by = 1

    if jumlah_coklat <= 0 and by == 1:
        by = 0
        
    
    result_contour_putih = cv2.drawContours(result,contours_putih,-1,(255, 0, 0), 2)
    result_contour_abuabu = cv2.drawContours(result,contours_abuabu,-1,(0,0,255), 2)
    result_contour_hitam = cv2.drawContours(result,contours_hitam,-1,(0, 255, 0), 2)
    result_contour_coklat = cv2.drawContours(result,contours_coklat,-1,(0, 255, 255), 2)

    cv2.imshow("kamera",result)
    if cv2.waitKey(10) & 0xFF == 27:
        ser.write(b"0")
        ser.close()
        