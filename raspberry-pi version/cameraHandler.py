from picamera import PiCamera
from time import sleep

def cameraHandler(imagenumber,workingdir,camera):
    capturepath=workingdir+"/img"+str(imagenumber)+".bmp"
    #camera=PiCamera()
    #As defining camera in here place's it in a loop and full's GPU memory
    #I defined it in main file and passed as a parameter to this function.
    
    #camera.rotation=90
    camera.contrast=100
    camera.brightness=10
    camera.resolution=(1024,768)
    camera.framerate=15
    camera.start_preview(alpha=200)
    #camera.brightness=70
    sleep(5)
    camera.capture(capturepath)
    camera.stop_preview()
    return(capturepath)