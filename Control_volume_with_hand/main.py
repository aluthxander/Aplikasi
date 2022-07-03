from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from comtypes import CLSCTX_ALL
from ctypes import cast, POINTER
import numpy as np
import cv2
import mediapipe as mp
import time
import HandTracker as htm
import math
# ===========================
# mengatur tinggi dan lebar perekaman
wCam, hCam = 640, 480
cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
# ==========================
pTime = 0
detector = htm.handDetector()

# volume speaker
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

# variable-variabel untuk pengaturan volume awal
volRange = volume.GetVolumeRange()
minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 400
volPercent = 0

while True:
    # mendeteksi adanya tangan pada rekaman
    succes, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # membaca output koordinat pada ujung jari telunjuk dan ibu jari
        # print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]
        # membuat koordinate lingkaran tengah
        cx, cy = (x1+x2)//2, (y1+y2)//2
        # lingkaran pada ujung jari telunjuk
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        # lingkaran pada ujung ibu jari
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)
        # garis antara ujung jari telunjuk dan ibu jari
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 2)
        # lingkaran pada tengah garis
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)

        # mencari garis Euclidean
        length = math.hypot(x2-x1, y2-y1)
        # hand range 50-300
        # Volume Range -65 - 0
        # melakukan konversi nilai length ke nilai2 volume
        # nilai volume device
        vol = np.interp(length, [50, 300], [minVol, maxVol])
        # volume bar
        volBar = np.interp(length, [50, 300], [400, 150])
        # volume dalam persen
        volPercent = np.interp(length, [50, 300], [0, 100])
        print(int(length), vol)
        # mengatur volume pada device
        volume.SetMasterVolumeLevel(vol, None)

        if length < 50:
            cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

    # membuat kotak volume pada perekaman
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 2)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPercent)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # membuat nilai FPS
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (40, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    # menghentikan perekaman
    cv2.imshow("img", img)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
