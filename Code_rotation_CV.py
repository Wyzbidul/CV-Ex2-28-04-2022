#####################################################################################################################################
#	PROGRAM BY : MC IATRIDES
#	LAST UPDATE : 28-04-2022
#	TITLE : Exercise #2 - (28-04-2022)
#   SUBTITLE : Image rotation with OpenCV
#	REDACTED FOR : COMPUTER VISION
#####################################################################################################################################

##### PACKAGES ######################################################################################################################
from numpy import *
import cv2 as cv
#####################################################################################################################################

###### ANALYSIS PART ################################################################################################################
print('START TESTS')


#Import original image into the program
img = cv.imread("Tower_of_Pisa.jpg")
height, width, _ = img.shape

#Display the original image
cv.imshow('input', img)
cv.waitKey(0)

#Generate rotation matrix from desired characteristics
M = cv.getRotationMatrix2D((width / 2, height / 2), 45, 0.5)
M = append(M, [0,0,1])
M = reshape(M, (3,3))

#Modify pixels to obtain final rotation
dst = cv.warpPerspective(img, M, (width, height))

#Display the resulting image
cv.imwrite('output_rotation.jpg',dst)
cv.imshow('output',dst)
cv.waitKey(0) 
cv.destroyAllWindows()

print('END TESTS')
#####################################################################################################################################
