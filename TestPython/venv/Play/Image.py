import cv2

im_g = cv2.imread("C:/Users/yarona/Downloads/smallgray.png" ,1)
print(im_g)

cv2.imwrite("C:/Users/yarona/Downloads/smallgray2.png" , im_g) #copy orig Image


#itreation on numpy
for i in im_g:
     print(i)

for i in im_g.flat:
     print(i)

#Scliding
print (im_g[0:2,2:4])



