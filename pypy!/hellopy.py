import cv2 as cv
from matplotlib import pyplot as plt
#defind the img and read
img = cv.imread('img.jpg')
#print the img
plt.imshow(cv.cvtColor(img,cv.COLOR_BGR2RGB))
plt.title('Rampo<3')
plt.axis('on')
plt.show()





#cv.imshow("window",img)
#the wait?
#cv.waitKey(0)
#cv.destroyAllWindow()
