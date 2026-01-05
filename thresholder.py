import cv2
import numpy as np
from skimage import feature
from skimage.util import img_as_ubyte

#create's a cnny threshold binary output
def thresholder(final,model):
    #if noise is toomuch enable below line
    #final = cv.medianBlur(final,3)
    
    #Ido not remember why "eedges" variable was declared, but looks like's it is good for better results.
    #L2gradient=True cause to linking edges and better closed lines for detection
    
    eedges=0
    val=np.ravel(final)
    modifiedval=np.delete(val,np.where(val==255))
    mean=int(modifiedval.mean())
    std=int(modifiedval.std())
    print("mean:",mean)
    print("std:",std)
    
    
    
    
    if model==1:
        filtersize=3
        minThreshold=mean-(0.80*std)
        minThreshold=int(minThreshold)
        print("tresh:",minThreshold)
        maxThreshold=-1
        edges=cv2.Canny(final,eedges,minThreshold,maxThreshold,filtersize,L2gradient=True)
    elif model==2:
        edges= feature.canny(final,sigma=0)
        edges = img_as_ubyte(edges)

    
    #edges=cv2.Canny(final,eedges,100,-1,3,L2gradient=True)
    imS = cv2.resize(edges, (700, 500))
    cv2.imshow("Canny", imS)
    cv2.waitKey(5000)
    cv2.destroyAllWindows()
    cv2.imwrite("canny.jpg",edges)

    return(edges)