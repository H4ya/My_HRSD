import cv2
import requests
source='https://youtube.com/shorts/9fF542ekFo8?si=7s8wd2leZukZeedE'
video_file = 'downloaded_video.mp4'  # Adjust filename as needed

# Download video
response = requests.get(source, stream=True)
with open(video_file, 'wb') as f:
    for chunk in response.iter_content(chunk_size=1024):
        f.write(chunk)

# Face detection (with potential fixes as mentioned previously)
fdet = cv2.CascadeClassifier('myfacedetector.xml')  # Check file path
cape = cv2.VideoCapture(video_file)
if not cape.isOpened:
    print("Errror!")
    exit()
color=(149, 53, 83)
thi=5
while True:
    ret,img= cape.read()
    if not ret:
        print("cant read src")
        break

    gray =cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces=fdet.detectMultiScale(gray,scaleFactor=1.1,minNighbors=4)

    for (x,y,w,h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
    cv2.imshow(source,img)
    cv2.waitKey(30)
    key=cv2.waitKey(1)&0xFF
    if key == 27:
        break
cape.release()
cv2.destroyAllWindows()

