#Works only for black background
import cv2
#Read The Image
img = cv2.imread(r'50.png')

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('GRAYSCALE Image',grayscale)
ret,thresholded = cv2.threshold(grayscale, 253, 255, cv2.THRESH_OTSU)

cv2.imshow('Threshold Image',thresholded)

bbox = cv2.boundingRect(thresholded)

x, y, w, h = bbox

print(bbox)

foreground = img[y:y+h, x:x+w]

#cv2.imwrite("foreground.png", foreground)
cv2.imshow('Cropped Image',foreground)
cv2.waitKey(0)
cv2.destroyAllWindows()
