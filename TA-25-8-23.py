import cv2
import numpy as np
from pygame import mixer
from time import sleep

#definisi variabel
b   = 0
bb  = 0
bg  = 0
by  = 0
b2  = 0
lower_putih = 0
upper_putih = 0
lower_abu = 0
upper_abu = 0
lower_coklat = 0
upper_coklat = 0
lower_hitam = 0
upper_hitam = 0


cap = cv2.VideoCapture(1)
mixer.init()

def nothing(x):
    pass
    
# memunculan window kalibrasi 
cv2.namedWindow("Kalibrasi")
cv2.createTrackbar("LowerHue", "Kalibrasi", 0, 255, nothing)
cv2.createTrackbar("LowerSatu", "Kalibrasi", 0, 255, nothing)
cv2.createTrackbar("LowerValue", "Kalibrasi", 0, 255, nothing)
cv2.createTrackbar("UpperHue", "Kalibrasi", 255, 255, nothing)
cv2.createTrackbar("UpperSatu", "Kalibrasi", 255, 255, nothing)
cv2.createTrackbar("UpperValue", "Kalibrasi", 255, 255, nothing)

# memunculkan window jenis warna
cv2.namedWindow("Warna")
cv2.createTrackbar("Putih", "Warna", 0, 1, nothing)
cv2.createTrackbar("Abu-abu", "Warna", 0, 1, nothing)
cv2.createTrackbar("Coklat", "Warna", 0, 1, nothing)
cv2.createTrackbar("Hitam", "Warna", 0, 1, nothing)



while True:
    check, image = cap.read()
    #image = cv2.imread("rgb.png")
    # pengali = 1
    # x = image.shape[1] * pengali
    # y = image.shape[0] * pengali
    # dimensi = (x,y)
    # resize  = cv2.resize(image,dimensi)

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # menentukan nilai HUE,SATURATION AND VALUE
            #=====>lower
    LowerHue = cv2.getTrackbarPos("LowerHue", "Kalibrasi")
    LowerSaturation = cv2.getTrackbarPos("LowerSatu", "Kalibrasi")
    LowerValue = cv2.getTrackbarPos("LowerValue", "Kalibrasi")
            #=====>Upper 
    UpperHue = cv2.getTrackbarPos("UpperHue", "Kalibrasi")
    UpperSaturation = cv2.getTrackbarPos("UpperSatu", "Kalibrasi")
    UpperValue = cv2.getTrackbarPos("UpperValue", "Kalibrasi")

    putih_slide = cv2.getTrackbarPos("Putih", "Warna")
    abu_slide = cv2.getTrackbarPos("Abu-abu", "Warna")
    coklat_slide = cv2.getTrackbarPos("Coklat", "Warna")
    hitam_slide = cv2.getTrackbarPos("Hitam", "Warna")

     # lower &upper for HSV image 
    # l_b = np.array([LowerHue, LowerSaturation, LowerValue])
    # u_b = np.array([UpperHue, UpperSaturation, UpperValue])

    #Range warna 
    lower = np.array([LowerHue,LowerSaturation,LowerValue])
    upper = np.array([UpperHue,UpperSaturation,UpperValue])
    mask = cv2.inRange(hsv, lower, upper)
    
    if putih_slide == 1 :
        lower_putih = lower
        upper_putih = upper

    if abu_slide == 1 :
        lower_abu = lower
        upper_abu = upper

    if coklat_slide == 1 :
        lower_coklat = lower
        upper_coklat = upper

    if hitam_slide == 1 :
        lower_hitam = lower
        upper_hitam = upper

    mask_putih = cv2.inRange(hsv, lower_putih, upper_putih)
    edge_putih = cv2.Canny(mask_putih,240,255)

    mask_abu = cv2.inRange(hsv, lower_abu, upper_abu)
    edge_abu = cv2.Canny(mask_abu,240,255)

    mask_coklat = cv2.inRange(hsv, lower_coklat, upper_coklat)
    edge_coklat = cv2.Canny(mask_coklat,240,255)

    mask_hitam = cv2.inRange(hsv, lower_hitam, upper_hitam)
    edge_hitam = cv2.Canny(mask_hitam,240,255)


    # edge_putih = cv2.Canny(mask_putih,240,255)

    # #Range warna Abu - Abu
    # lower_abuabu = np.array([0,0,40])
    # upper_abuabu = np.array([84,16,221]) 


    # #Range warna Hitam
    # lower_hitam = np.array([0,0,0])
    # upper_hitam = np.array([180,255,50])
    # mask_hitam = cv2.inRange(hsv, lower_hitam, upper_hitam)
    # edge_hitam = cv2.Canny(mask_hitam,240,255)

    # #Range warna Coklat
    # lower_coklat = np.array([10, 100, 20])
    # upper_coklat = np.array([20, 255, 200])
    # mask_coklat = cv2.inRange(hsv, lower_coklat, upper_coklat)
    # edge_coklat = cv2.Canny(mask_coklat,240,255)


    contours_putih , hierarchy = cv2.findContours(edge_putih,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours_abu , hierarchy2 = cv2.findContours(edge_abu,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours_hitam , hierarchy3 = cv2.findContours(edge_hitam,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    contours_coklat , hierarchy4 = cv2.findContours(edge_coklat,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)


    jumlah_putih  = len(contours_putih)
    jumlah_abu = len(contours_abu)
    jumlah_hitam = len(contours_hitam)
    jumlah_coklat = len(contours_coklat)
 
    # jumlahWarna : int
    # jumlahWarna = ((jumlah_putih + jumlah_abu + jumlah_hitam + jumlah_coklat))
    
    # if jumlah_putih != 0 and b == 0:
    #     if not mixer.music.get_busy():
    #         mixer.music.load("adaputih.mp3")
    #         mixer.music.play()
    #     else:
    #         sleep(2)
    #         mixer.music.load("adaputih.mp3")
    #         mixer.music.play()
    #     print("Putih")
    #     b = 1

    # if jumlah_putih <= 0 and b == 1:
    #     b = 0

    # if jumlah_abu != 0 and bb == 0:
    #     if not mixer.music.get_busy():
    #         mixer.music.load("adaabuabu.mp3")
    #         mixer.music.play()
    #     else:
    #         sleep(2)
    #         mixer.music.load("adaabuabu.mp3")
    #         mixer.music.play()
    #     print("Abu - Abu")
    #     bb = 1

    # if jumlah_abu <= 0 and bb == 1:
    #     bb = 0

    # if jumlah_hitam != 0 and bg == 0:
    #     if not mixer.music.get_busy():
    #         mixer.music.load("adahitam.mp3")
    #         mixer.music.play()
    #     else:
    #         sleep(2)
    #         mixer.music.load("adahitam.mp3")
    #         mixer.music.play()
    #     print("Hitam")
    #     bg = 1

    # if jumlah_hitam <= 0 and bg == 1:
    #     bg = 0

    # if jumlah_coklat != 0 and by == 0:
    #     if not mixer.music.get_busy():
    #         mixer.music.load("adacoklat.mp3")
    #         mixer.music.play()
    #     else:
    #         sleep(2)
    #         mixer.music.load("adacoklat.mp3")
    #         mixer.music.play()
    #     print("Coklat")
    #     by = 1

    # if jumlah_coklat <= 0 and by == 1:
    #     by = 0
        
    cv2.imshow("kamera",image)
    cv2.imshow("mask",mask)
    cv2.waitKey(10)        