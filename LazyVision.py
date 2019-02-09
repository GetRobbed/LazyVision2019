from statistics import mean
import PIL
import numpy as np
#import *
from PIL import Image, ImageFilter
#import robo219
changeVal = 250
Is=np.array([], dtype=np.float64)
Js=np.array([], dtype=np.float64)
m=0
b=0
edge = 0
norm = 255
tempo = 0
#fswebcam -r 352x288 --no-banner /home/pi/webcam/currentImage.jpg
image = Image.open('/home/pi/webcam/currentImage.jpg').convert('L')
px = image.load()

#image.save('/home/pi/testing123.jpg')
width, height = image.size

if height > 287:
    cropped = image.crop((0,69,width,height))
    tempo = 69
else:
    cropped = image.crop((0,0,width,height))
    tempo = 0

cropped.save('/home/pi/webcam/currentImage.jpg')


imgAr = np.array(cropped)
temp = np.array(cropped)
def wrongWay():
    print(imgAr[0,0])
    for i in range(0,height-tempo):
        for j in range(1,width):
            if(abs((imgAr[i,j]-imgAr[i,j-1]))>changeVal):
                temp[i,j] = edge
            else:
                temp[i,j] = norm
            print('x')
            print (imgAr[i,j])
            print (i,j)
            print (abs((imgAr[i,j]-imgAr[i,j-1])))
    im = Image.fromarray(temp)
    im.save('/home/pi/webcam/gucci.jpg')
def maybeWay():
    
    Iso=[]
    Jso=[]
    test = cropped.filter(ImageFilter.FIND_EDGES)
    #test.save('/home/pi/webcam/gucci.jpg')
    temp = np.array(test)
    for i in range(0,height-tempo):
        for j in range(1,width):
            if (temp[i,j]<40):
                temp[i,j] = 0
            else:
                temp[i,j] = 255
                #
    for x in range(0,width):
        temp[0,x] = 0
        temp[1,x] = 0
    #
    for i in range(1,height-tempo-1):
        for j in range(1,width-1):
            if(temp[i,j]>0):
                if(temp[i+1,j] > 0 or temp[i-1,j] > 0 or temp[i,j+1]> 0 or temp[i,j-1]> 0 or temp[i+1,j+1]> 0 or temp[i-1,j-1] or temp[i+1,j-1]> 0 or temp[i-1,j+1]> 0):
                    temp[i,j] = 255
                    Iso.append(i)
                    Jso.append(j)
                else:
                    temp[i,j] = 0
                    #
    for x in range(0,width - tempo):
        temp[0,x] = 0
        temp[1,x] = 0
    #
    Is = np.asarray(Iso, dtype=np.float64)
    Js = np.asarray(Jso, dtype=np.float64)
    m= (mean(Is)*mean(Js)-mean(Js*Is))/((mean(Is)*mean(Is))-mean(Is*Is))
    b= mean(Js)-m*mean(Is)
    #
    print(m)
    print(b)
    for j in range(0,height-tempo):
        guccigang = int(m*j+b)
        if(abs(guccigang)<352):
            temp[j,guccigang]=255
        else:
            print("Hello World")
    #for y in range(0,height):
    #    temp[int((y-b)/m),y] = 255
    test = Image.fromarray(temp)
    test.save('/home/pi/webcam/gucci.jpg')
    #for j in range(1,width):
    #    temp[m*j+b,j]
    return m
maybeWay()
return maybeWay()

#print(imgAr)
            
            
