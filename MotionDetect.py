import numpy as np   #Matematikai fgv konyvtar beillesztese - Numerical Python
import cv2      #openCV beillesztese

vid = cv2.VideoCapture('sample.avi')  #Video v. kamerakep beolvasasa
ret, kepkocka0 = vid.read()    #Video elso ket kepkockajanak kinyerese es valtozoba toltese
ret, kepkocka1 = vid.read()

while vid.isOpened():   #Ciklus amelyben a videokep elemzesre kerul (a video vegeig vagz "Esc" megnzyomasaig
    kulonbseg = cv2.absdiff(kepkocka0, kepkocka1)  #Egymast koveto kepkockak kozti kulonbsegek meghatarozasa
        # Kulonbseg es elkereses folyamata
    grayscl = cv2.cvtColor(kulonbseg, cv2.COLOR_BGR2GRAY)   #Kulonbseg konvertalasa szurkearnyalatos modba
    gausselmos = cv2.GaussianBlur(grayscl, (3,3), 0) #Szurkearnyalatos kep gauss elmosasa ahol a kernel 3x3-as az x es y iranyu eltolas 0
    _, kuszob = cv2.threshold(gausselmos, 50, 255, cv2.THRESH_BINARY) # Kuszobertek meghatarozasa binaris kepen
    dilatacio = cv2.dilate(kuszob, None, iterations=2)    #Morfologiai eljaras az elek folytonossa tetelere dilatacioval ketszer vegrehajtva
    _, elek, _ = cv2.findContours(dilatacio, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) #Elek meghatarozasa
        # Detektalt elek megjelolese a kepkockan
    cv2.drawContours(kepkocka0,elek,-1,(0,0,255),2)    #piros es 2 pixel vastag jeloles
    cv2.imshow('Motion Detect',kepkocka0)  #Kepkocka megjelenitese a detektalt elek megjelolesevel
    kepkocka0 = kepkocka1     #Kepkockak tovabb leptetese
    ret, kepkocka1 = vid.read()    #Kovetkezo kepkocka kiolvasasa (a ciklus elso lefutasa eseten a harmadik kepkocka)

    if cv2.waitKey(40) == 27:   #Ciklusbol valo kilepes "Esc" megnyomasara
        break

cv2.destroyAllWindows() #Video ablak bezarasa
vid.release()   #Videot v. kamerakepet tartalmazo valtozo felszabaditasa


