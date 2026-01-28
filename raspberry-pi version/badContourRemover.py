from math import pi
from cv2 import contourArea
from cv2 import arcLength
import cv2
import numpy as np

def badcontourremover(r,contours2,hierarchy2,black):
    #create deciding variables
    cn=0
    
    s=pi*(r**2)
    plateperimeterlimit=(r/2)*pi
    bb=black
    EE=black
    kernel = np.ones((2,2),np.uint8)

    ###detecting True parental level of objects###


    
    for cnt in contours2:
        cntt=0
        cntt=contours2[cn]
    
        #claculate contourrs area
        area=0.0
        area=contourArea(cntt)
    
        #calculate contour perimeter
        perimeter=0.0
        perimeter=arcLength(cntt,True)
        
        if perimeter < plateperimeterlimit:
            
            if area != 0:
                
                if area < s/2:
                    cv2.drawContours(bb, [cntt], -1, (255,255,255), 1)
                    
        cn=cn+1
    imS = cv2.resize(bb, (700, 500))
    #cv2.imshow("Extra 1", imS)
    #cv2.waitKey(5000)
    #cv2.destroyAllWindows()

    contoursExtera , hierarchyExtra= cv2.findContours(bb, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.drawContours(EE, contoursExtera, -1, (255,255,255), 1)
    EE=cv2.morphologyEx(EE, cv2.MORPH_CLOSE, kernel)
    imSs = cv2.resize(EE, (700, 500))
    #cv2.imshow("Extra2", imSs)
    #cv2.waitKey(5000)
    #cv2.destroyAllWindows()
    
    return(contoursExtera)
