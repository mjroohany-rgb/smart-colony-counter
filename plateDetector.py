import cv2
import numpy as np

#this madule contain's two function-plateBorderFinder find plate circle and mark it-plateCropper mask the selected are with a circle and remove waste regions.
#this two functions originated from stackOverFllow and also some other parts of this code too.
def plateBorderFinder(gray_blurred,img,hh,minr):
    
    # Apply Hough transform on the blurred image. 
    #jj in here "hh" is inputed image's bigest dimention and is minmum distance between of detected circles center
    # and "minr" is minimum radius of circles "minr=int(h/4)"
    # this two parameters cause to detecting plate's border circle very nicely in most cases
    detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, hh, param1 = 50, param2 = 30, minRadius = minr, maxRadius = 0) 
    
    # Draw circles that are detected. 
    if detected_circles is not None: 
    
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
        
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
            
            # Draw the circumference of the circle. 
            cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
            
            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(img, (a, b), 1, (255, 0, 0), 3)
    imcircle = cv2.resize(img, (700, 500))
    cv2.imshow("Detected Circle", imcircle)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    return(detected_circles,a,b,r)
    
def plateCropper(gray_blurred,a,b,r):
    #this function crop circular area taht belong's to plate.according to plateBorderFinder
    # create a mask
    mask = np.full((gray_blurred.shape[0], gray_blurred.shape[1]), 0, dtype=np.uint8) 
    
    # create circle mask, center, radius, fill color, size of the border
    cv2.circle(mask,(a,b), r, (255,255,255),-1)
    
    # get only the inside pixels
    fg = cv2.bitwise_or(gray_blurred, gray_blurred, mask=mask)

    mask = cv2.bitwise_not(mask)
    
    background = np.full(gray_blurred.shape, 255, dtype=np.uint8)
    
    bk = cv2.bitwise_or(background, background, mask=mask)
    
    final = cv2.bitwise_or(fg, bk)
    imS = cv2.resize(final, (700, 500))
    cv2.imshow("Cropped Circle", imS)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    return(final)