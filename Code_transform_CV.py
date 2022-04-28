#####################################################################################################################################
#	PROGRAM BY : MC IATRIDES
#	LAST UPDATE : 28-04-2022
#	TITLE : Exercise #2 - (28-04-2022)
#   SUBTITLE : Image transformation with OpenCV
#	REDACTED FOR : COMPUTER VISION
#####################################################################################################################################

##### PACKAGES ######################################################################################################################
from numpy import *
import cv2 as cv
#####################################################################################################################################

###### ANALYSIS PART ################################################################################################################
print('START TESTS')

#Import original image into the program
img = cv.imread("MM.jpg")
height, width, _ = img.shape

#Display the original image
cv.imshow('input', img)
cv.waitKey(0)

#Input points that represent original and final positions of desired transformation
pts1 = float32([[282, 71], [613, 277], [244, 579], [656, 595]])
pts2 = float32([[280, 70], [600, 70], [280, 700], [600, 700]])

#Transform points from original to final position and modify the rest of the pixels accordingly
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img, M, (900, 900)) 

#Display the resulting image
cv.imwrite('output_transform.jpg',dst)
cv.imshow('output',dst)
cv.waitKey(0)
cv.destroyAllWindows()

print('END TESTS')
#####################################################################################################################################
