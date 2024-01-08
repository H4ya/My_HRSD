import telebot
import cv2
import numpy as np
from telebot import types

bot=telebot.TeleBot('1220799704:AAEp94Vq54n-MbPvlvQU2PXqDM_Bqbell1g')

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    file_id = message.photo[-1].file_id
    file_info = bot.get_file(file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    with open("photo.jpg",'wb') as new_file:
        new_file.write(downloaded_file)

    img=cv2.imread("photo.jpg")

    gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30,30))

    for (x, y, w, h) in faces:
        face_roi = gray[y:y +h,x:x+w]
        edges = cv2.Canny(face_roi,50,150)
        lines= cv2.HoughLinesP(edges,1,np.pi/180,threshold=50,minLineLength=30,maxLineGap=10)

        if lines is not None:

            cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

            cv2.imwrite("result.jpg",img)

            with open("result.jpg",'rb') as result_file:    
                bot.send_photo(message.chat.id,result_file,"Found ya!")
            return

    bot.reply_to(message,"ALL CLEAR!")
    
if __name__ == "__main__":
    bot.polling(none_stop=True)

#perfect- almost
#مدري كيف اخليه يحدد حتى اللي ماعنده جوال