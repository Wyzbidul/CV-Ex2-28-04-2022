from numpy import *
import cv2

#Import original image into the program
img = cv2.imread("Tower_of_Pisa.jpg")
height, width, _ = img.shape

#Display the original image
cv2.imshow('input', img)
cv2.waitKey(0)

#Generate rotation matrix from desired characteristics
M = cv2.getRotationMatrix2D((width / 2, height / 2), 45, 0.5)
M = append(M, [0,0,1])
M = reshape(M, (3,3))

#Modify pixels to obtain final rotation
dst = cv2.warpPerspective(img, M, (width, height))

#Display the resulting image
cv2.imwrite('output.jpg',dst)
cv2.imshow('output',dst)
cv2.waitKey(0) 
cv2.destroyAllWindows()