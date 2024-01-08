import cv2 
import numpy as np
import matplotlib.pyplot as plt
import requests
from PIL import Image

car_cascade = cv2.CascadeClassifier('cars.xml')

source='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR02hdzWGrA8H06sa0PdRiizVFp7MU9qaDllpHc9mzGdbs6mgsFePLDbjPJhg&s'
img = Image.open(requests.get(source,stream=True).raw)

img = img.resize((450,250))

imgarr=np.array(img)

gray =cv2.cvtColor(imgarr,cv2.COLOR_BGR2GRAY)

cars = car_cascade.detectMultiScale(gray, 1.1 ,1)

car_count =0 
for (x,y,w,h) in cars:
    cv2.rectangle(imgarr, (x, y), (x+w, y+h), (0, 255, 0), 2)
    car_count+=1

plt.imshow(cv2.cvtColor(imgarr,cv2.COLOR_BGR2RGB))
plt.title("detected cars!")
plt.axis('off')

plt.show()
print(f'number of detected cars {car_count}')
