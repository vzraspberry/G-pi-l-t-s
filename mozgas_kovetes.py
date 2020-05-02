import cv2  #openCV meghívás
import numpy  #matematikai csomag meghívás

record = cv2.VideoCapture('test.mp4')  #"record" objektum létrehozás, videó betöltés

while record.isOpened():
    ret, frame = record.read()  #Beolvasás képkockánként
    
    cv2.imshow('frame', frame)  #Ablak neve és az adott képkocka
    
    if cv2.waitKey(40) == 27:  #ESC-re kilép
        break
        
cv2.destroyAllWindows()  #ablak bezárása
record.release()  #videó adatok törlése a memóriából