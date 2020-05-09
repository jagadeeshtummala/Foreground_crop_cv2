# This Code converts the white background into Black so we can use for Cropping the Freground(Object)
import numpy as np
import cv2
import matplotlib.pyplot as plt
%matplotlib inline

img=cv2.imread(r'Photos1\50.jpg')
img=cv2.resize(img,(img.shape[1]//8,img.shape[0]//8),cv2.INTER_CUBIC)
print(img.shape)
mask=np.zeros(img.shape[:2],np.uint8)

bgdModel=np.zeros((1,65),np.float64)
fgdModel=np.zeros((1,65),np.float64)
rect=(20,20,img.shape[1]-50,img.shape[0]-50)  # Change The rectangle values accoding to the Object Position in Image
img1=img.copy()
cv2.rectangle(img1,(20,20),(img.shape[1]-30,img.shape[0]-30),(255,0,255),2)
cv2.grabCut(img,mask,rect,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)
mask2=np.where((mask==2)|(mask==0),0,1).astype('uint8')
img=img*mask2[:,:,np.newaxis]
cv2.imshow('Image',img)
cv2.imshow('Image1',img1)
cv2.imwrite(r'Test_images\50.png',img)
#cv2.imshow('Image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
