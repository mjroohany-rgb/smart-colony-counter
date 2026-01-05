#this function filters counters by size and parent and child relationship and then draw them

import cv2
from math import pi
import numpy as np
import math
def contoursDrawer(r,contoursExtera,imagefinal,imagenumber,workingdir,h,w,contoursExtraLen,comtours2len,model):
    ###set deciding variables###
    cn=0
    mergedcount=0.0
    s=0.0
    s=pi*(r**2)
    #print("S is:",s)
    plateperimeterlimit=0.0
    plateperimeterlimit=(r/2)*pi
    #print("plateperimeterlimit is:",plateperimeterlimit)
    zerocount=0
    decider=True    

    cflperimeter=0.0
    cflminarea=0.0
    cflmaxarea=0.0
    cflparent=0.0

    lent=len(contoursExtera)

    childcount=0
    truecirclecount=0
    

    totalmergedarea=0.0

    convexitycount=0

    drawcount=0
    

    totalarea=0.0
    #filter by cicularity 0.90 fure surface plate and 0.50 for pure plate
    #filter by convexity 0.95 fure surface plate and 0.85 for pure plate
    #that two lines are old comments
    

    #for surface olate

    goodcircle1 = 0.50
    goodconvex1 = 0.90
    if model==1:
        asx=4
    elif model==2:
        asx=2

 
        ###drawing circle and convex Objects###
    #this for loop runes for each contour
    for cnt in contoursExtera:
        
        
    
        decider=True
        cntt=0
        cntt=contoursExtera[cn]
        
        counterboom= np.zeros((h, w, 1), dtype = "uint8")
        cv2.drawContours(counterboom, [cntt], -1, (255,255,255), 1)
        imtemp = cv2.resize(counterboom, (700, 500))
        #cv2.imshow("temp contour", imtemp)



        drawed=False
    
        #claculate contours area
        area=0.0
        area=cv2.contourArea(cntt)
        totalarea=totalarea+area
        #print("area is:", area)
        #calculate contour perimeter
        perimeter=0.0
        perimeter=cv2.arcLength(cntt,True)
        #print("perimeter is:",perimeter)
        #print("number:",cn)
        
    
        #removing contpurs with perimeter bigger than half of plate
        if perimeter > plateperimeterlimit:
            decider=False
            cflperimeter=cflperimeter+1
            #print("BIGGER than plateperimeterlimit")
        
        #removing contours with small area because they are not true colonies
      

        

        
        #removing objects with area bigger than half of plate
        if area > s/2:
            decider=False
            cflmaxarea=cflmaxarea+1
            #print("bigger than s/2")
    
        if decider == False:
            
            zerocount=zerocount+1
        else:
            #removing objects that are not closed shapes
            
            
            #aspectratio helps to detecting merged objects in future if statement
            aspectratio = ((perimeter**2)/((4*pi)*area))
            #print("aspect ratio is:", aspectratio)
    
            #Circulariry is a number between 0 and 1
            #for a complete circle is 1 for a square is about 0.785
            #and for a line is 0
            circularity=((4*pi)*area)/((perimeter)**2)
            #print("circularity is:", circularity)
#checking process Circularity---> if not ---> convexity AND then merged or not ---> if not ---> cheking merged or not
            if circularity >= goodcircle1:

                #if object doesn't pass circularity then we check it with
                #convexity it is number between 0 and 1
                hull=cv2.convexHull(cntt)
                hullarea=cv2.contourArea(hull)
                convexity=area/hullarea
                #print("bad circle")
                #print("hullarea is:", hullarea)
                #print("convexity is:",convexity)
                
                #filter contours by convexity
                if convexity >= goodconvex1:
                    #print("good convex 1")
                    #cheking convex contours for merge
                    #if aspect ratio for convex contours is smallers than this number it is merged and will draw red
                    if circularity >= goodcircle1:
                        if aspectratio >= 1.7:
                            if model != 2:
                                roundit=math.floor(aspectratio)
                                mergedcount=mergedcount+roundit
                                cv2.drawContours(imagefinal, [cntt], -1, (0,0,255), 2)
                                drawed=True
                                #print("R1-1:",roundit)
                                #this variable store's total area of merged contours for approximation merged contours number
                                #print("rounded:",roundit)
                                #print("merged")
                        elif aspectratio < 1.7:
                            convexitycount=convexitycount+1
                            cv2.drawContours(imagefinal, [cntt], -1, (0,255,0), 2)
                            drawed=True
                            #print("R1-2: Single")

                    #if convex is not merged will draw green
                    elif circularity < goodcircle1:
                        if aspectratio < 3:
                            if model != 2:
                                roundit=math.floor(aspectratio)
                                mergedcount=mergedcount+roundit
                                cv2.drawContours(imagefinal, [cntt], -1, (0,0,255), 2)
                                drawed=True
                            #print("R2:",roundit)
                        #print("single")
                # if convexity is small then will be checked for merged or not    
                elif convexity < goodconvex1:
                    #print("good convex 2")
                    #check merged or not
                    if aspectratio < asx:
                        
                        roundit=math.floor(aspectratio)
                        mergedcount=mergedcount+roundit
                        #print("round:",roundit)
                        cv2.drawContours(imagefinal, [cntt], -1, (0,0,255), 2)
                        drawed=True
                        totalmergedarea=totalmergedarea+area
                        #print("R3:",roundit)
                        
   

        
        
        #counting drawed contours
        if drawed == True:
            drawcount=drawcount+1

        circularity=0.0
        
        cn=cn+1
        #cv2.waitKey(10000)
        #print("------------------------")

        
    
    
    areaTNTC=totalarea/s
    #generating results report and storing it in formatted "results" variable for showing it in a message
    
    

  
    lastResult=truecirclecount+convexitycount+mergedcount
    results="True Circles:"+ str(truecirclecount)+"\n"
    results=results+"Single Convexes:"+str(convexitycount)+"\n"
    results=results+"Merged Approximation:"+str(mergedcount)+"\n"
    results=results+"total colonies number="+str(lastResult)+"\n"
    
    #comtours22len=comtours2len*0.60
    
    if lastResult > 600:
        results=results+"this is a TNTC plate \n"
    elif areaTNTC >= 0.10:
        results=results+"may be it is a TNTC plate \n"    
    elif contoursExtraLen > 600:
        results=results+"may be it is a TNTC plate \n"
    elif comtours2len > 900:
        results=results+"may be it is a TNTC plate \n"
    print("areaTNTC:",areaTNTC)
    print("contoursExtraLen",contoursExtraLen)
    print("comtours2len:",comtours2len)
    
    #save image in workking directory
    savedirectory=workingdir+"/finalcolonies"+str(imagenumber)+".jpg"
    cv2.imwrite(savedirectory,imagefinal)
    #returning final cmarked iamge and counting results
    
    return(imagefinal,results)
