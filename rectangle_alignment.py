#align the given image and give figure name in accordance to the ascending order of the length of the line in it.

# from turtle import width
import cv2 as cv
from cv2 import CV_32F
import numpy as np


img=cv.imread("C:\\Users\\\Hp\\Documents\\opencv\\imagealign.png")


#declaring width and height of the image 
#here i calculated the width and height of the image
weidth,height=150,30
weidth1,height1=143,66
weidth2,height2=159,60
weidth3,height3=174,112


#this is the corner pixel of the original image 
pt=np.float32([[170,128],[315,166],[161,164],[306,203]])
pnt=np.float32([[435,156],[572,118],[452,219],[591,181]])
pint=np.float32([[131,398],[268,319],[161,451],[299,370]])
point=np.float32([[480,325],[631,411],[424,421],[575,507]])


# pt=np.float64(pt)
print(pt)


#this is the corner pixel that we define for the aligned image
pto=np.float32([[0,0],[weidth,0],[0,height],[weidth,height]])
pnto=np.float32([[0,0],[weidth1,0],[0,height1],[weidth1,height1]])
pinto=np.float32([[0,0],[weidth2,0],[0,height2],[weidth2,height2]])
pointo=np.float32([[0,0],[weidth3,0],[0,height3],[weidth3,height3]])
# pto=np.float64(pto)
print(pto)

#transformation for first figure in real image
transform_mat=cv.getPerspectiveTransform(pt,pto)
imgoutput=cv.warpPerspective(img,transform_mat,(weidth,height))


#transformation for second figure of real image
transform_mat1=cv.getPerspectiveTransform(pnt,pnto)
imgoutput1=cv.warpPerspective(img,transform_mat1,(weidth1,height1))

#for third figure of real image
transform_mat2=cv.getPerspectiveTransform(pint,pinto)
imgoutput2=cv.warpPerspective(img,transform_mat2,(weidth2,height2))

#for fourth figure of real image
transform_mat3=cv.getPerspectiveTransform(point,pointo)
imgoutput3=cv.warpPerspective(img,transform_mat3,(weidth3,height3))



#to draw margin at the corners of the image we do....
for x in range (0,4):
    cv.circle(img,(int(pt[x][0]),int(pt[x][1])),5,(0,255,255),cv.FILLED)
    cv.circle(img,(int(pnt[x][0]),int(pnt[x][1])),5,(255,255,0),cv.FILLED)
    cv.circle(img,(int(pint[x][0]),int(pint[x][1])),5,(0,0,255),cv.FILLED)
    cv.circle(img,(int(point[x][0]),int(point[x][1])),5,(255,0,0),cv.FILLED)

# cv.circle(img,(pt[0][0],pt[0][1]),5,(0,255,255),cv.FILLED)

#showing aligned images
cv.imshow("original image is:",img)
cv.imshow("The output image is:",imgoutput)
cv.imshow("The second output image is:",imgoutput1)
cv.imshow("The third output image is:",imgoutput2)
cv.imshow("The Third output image is:",imgoutput3)



#to hold the output window bar until letter q is pressed
while True:
    if cv.waitKey(1)==ord('q'): 
        break
