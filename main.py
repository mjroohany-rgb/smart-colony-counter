#this is the main source file of colony counter software
#author=mohammadJavad Rouhanifar

#import necessary libraries
import easygui
import cv2
#from picamera import PiCamera
from time import sleep
import gc
import numpy as np
import statistics

#import handWritten madules
import plateDetector
import thresholder
import contoursDrawer
#import cameraHandler
import badContourRemover



#set camera for later use in camera handler
#This must seted in cameraHnadler but because of that placing this line
# in a loop make's GPU full and camera unavalabe; so we define it here and use it in cameraHandler as a parameter.

#camera=PiCamera()

#imagenuber variable make's different naming for imagefiles
imagenumber=0

model=1
#selecting image source-localfile or camera
#seter = easygui.buttonbox(msg="Please select Image source",choices=('CAMERA','IMAGE FILE ON DISCK'))
seter = "IMAGE FILE ON DISCK"


#directory for saving output files
workingdir = easygui.diropenbox(msg="Please select folder to save files",title="Choose working directory",default=None)


#whle circle for making softwar able to recount
retry=True
while retry==True:
    
    imagenumber=imagenumber+1
    
    if seter == "IMAGE FILE ON DISCK":
        
        # jj open dialog box to select file
        path = easygui.fileopenbox()

        # Read image from file or camera 
        img = cv2.imread( path, cv2.IMREAD_COLOR)
    elif seter == "CAMERA":
        path = cameraHandler.cameraHandler(imagenumber,workingdir,camera)
        
        img = cv2.imread( path, cv2.IMREAD_COLOR)



    
    #jj set some variables that depend on image size

    #get image size
    h, w, _ = img.shape
    minr=int(h/4)
    maxr=0.0

    # jj find images correct ratio for using in circleTransform
    if h > w:
        maxr=h
        hh=h
    elif h < w:
        maxr=w
        hh=w
        

# Convert to grayscale. 
    gray =0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    #gray = cv2.resize(gray,(2*maxr, 2*hh), interpolation = cv2.INTER_CUBIC)
    

    #jjreducing noise

    # Blur using 3 * 3 kernel.
    

    gray_blurred = gray
    
   
    #Calling plateBorderFinder function
    detected_circles=0
    a=0
    b=0
    r=0
    detected_circles,a,b,r=plateDetector.plateBorderFinder(gray_blurred,img,hh,minr)
    
    
    #calling plateCropper function
    final=0
    final=plateDetector.plateCropper(gray_blurred,a,b,r)
    
    #making image bigger & adapting related varaibles
    
    zoom=2
    final = cv2.resize(final,(zoom*w, zoom*h), interpolation = cv2.INTER_CUBIC)
    h=h*zoom
    w=w*zoom
    hh=hh*zoom
    maxr=maxr*zoom
    r=r*zoom
    
    finalbackup=final
    final=cv2.GaussianBlur(final,(5,5),0)
    
    savecroped=workingdir+"/cropped.jpg"
    cv2.imwrite(savecroped,final)


    
    #calling thresholder function
    edges=0
    edges=thresholder.thresholder(final,model)
    
    #cv2.imshow("Sobel??",edges)
    #cv2.waitKey(10000)
    
    #using thresholder function from open cv to find color contours and their hierarchy of parent and child relationship
    contours2=0
    hierarchy2=0
    contours2 , hierarchy2= cv2.findContours(edges, cv2.RETR_LIST
                                            , cv2.CHAIN_APPROX_SIMPLE)
    comtours2len=len(contours2)
    #calling goodParentFinder function
    black = np.zeros((h, w, 1), dtype = "uint8")
    contoursExtera=badContourRemover.badcontourremover(r,contours2,hierarchy2,black)
    contoursExtraLen=len(contoursExtera)
    

    #converting grayscale border cropped image to rgb for enabeling color marking on it
    imagefinal=0
    imagefinal=cv2.cvtColor(final,cv2.COLOR_GRAY2RGB)
    
    #calling contoursDrawer function
    imagefinal,results=contoursDrawer.contoursDrawer(r,contoursExtera,imagefinal,imagenumber,workingdir,h,w,contoursExtraLen,comtours2len,model)
    
    #resizing uotput image-showing resized image
    imS =0
    imS = cv2.resize(imagefinal, (700, 500))
    cv2.imshow("finalColonies", imS)
    cv2.waitKey(10000)
    
    #asking for recount or not
    repeat = easygui.buttonbox(msg=results,choices=('COUNT NEW PLATE','LOOK FOR SMALLER COLONIES'))
   
    cv2.destroyAllWindows()  
    #print(gc.collect())
    gc.collect()
    #CHEKING FOR RECOUNTING OR NOT
    
    if repeat == "COUNT NEW PLATE":
       retry=True
       del _,a,b,contours2,detected_circles,edges,final,gray,gray_blurred,h,hh,hierarchy2,imS,imagefinal,img,maxr,r,results,w
    elif repeat == "LOOK FOR SMALLER COLONIES":
        model=2
        final=finalbackup
        edges=0
        edges=thresholder.thresholder(final,model)
        
        #cv2.imshow("Sobel??",edges)
        #cv2.waitKey(10000)
        
        #using thresholder function from open cv to find color contours and their hierarchy of parent and child relationship
        contours2=0
        hierarchy2=0
        contours2 , hierarchy2= cv2.findContours(edges, cv2.RETR_LIST
                                                , cv2.CHAIN_APPROX_SIMPLE)
        
        #calling goodParentFinder function
        black = np.zeros((h, w, 1), dtype = "uint8")
        contoursExtera=badContourRemover.badcontourremover(r,contours2,hierarchy2,black)
        
        

        #converting grayscale border cropped image to rgb for enabeling color marking on it
        imagefinal=0
        imagefinal=cv2.cvtColor(final,cv2.COLOR_GRAY2RGB)
        
        #calling contoursDrawer function
        imagefinal,results=contoursDrawer.contoursDrawer(r,contoursExtera,imagefinal,imagenumber,workingdir,h,w,contoursExtraLen,comtours2len,model)
        
        #resizing uotput image-showing resized image
        imS =0
        imS = cv2.resize(imagefinal, (700, 500))
        cv2.imshow("finalColonies", imS)
        cv2.waitKey(15000)
        model=1
        repeat=easygui.msgbox(msg=results,title="results",ok_button='COUNT NEW PLATE')
        if repeat == "COUNT NEW PLATE":
            retry=True
        else:
            retry=False
        cv2.destroyAllWindows()  
        del _,a,b,contours2,detected_circles,edges,final,gray,gray_blurred,h,hh,hierarchy2,imS,imagefinal,img,maxr,r,results,w
        gc.collect()
    else:
        retry=False
        del _,a,b,contours2,detected_circles,edges,final,gray,gray_blurred,h,hh,hierarchy2,imS,imagefinal,img,maxr,r,results,w
        gc.collect()

