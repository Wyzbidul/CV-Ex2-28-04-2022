from cv2 import BORDER_REPLICATE
from numpy import *
import cv2

#Import original image into the program
img = cv2.imread("MM.jpg")
height, width, _ = img.shape

#Display the original image
cv2.imshow('input', img)
cv2.waitKey(0)

#Input points that represent original and final positions of desired transformation
pts1 = float32([[282, 71], [613, 277], [236, 693], [665, 643]])
pts2 = float32([[280, 70], [600, 70], [280, 700], [600, 700]])

#Transform points from original to final position and modify the rest of the pixels accordingly
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img, M, (900, 900)) 

#Display the resulting image
cv2.imwrite('output.jpg',dst)
cv2.imshow('output',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()