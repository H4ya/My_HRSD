import cv2
import numpy as np
import telebot
from telebot import types

# قم بتبديل 'YOUR_TELEGRAM_BOT_TOKEN' برمز البوت الخاص بك على تيليجرام الفعلي
TOKEN = '1220799704:AAEp94Vq54n-MbPvlvQU2PXqDM_Bqbell1g'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['photo'])
def handle_photo(message):
    # قم بتنزيل الصورة
    file_info = bot.get_file(message.photo[-1].file_id)
    downloaded_file = bot.download_file(file_info.file_path)

    # احفظ الصورة على القرص المحلي
    with open("photo.jpg", 'wb') as new_file:
        new_file.write(downloaded_file)

    # قم بتحميل الصورة باستخدام OpenCV
    image = cv2.imread("photo.jpg")

    # قم بتحويل الصورة إلى اللون الرمادي
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # قم بتحميل مصنف كاسكيد الذي يُستخدم لاكتشاف الوجوه مسبقًا
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # اكتشف الوجوه في الصورة
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

    # تحقق مما إذا كان يوجد شخص يحمل جوال في كل وجه تم اكتشافه
    for (x, y, w, h) in faces:
        face_roi = gray[y:y + h, x:x + w]
        edges = cv2.Canny(face_roi, 50, 150)
        lines = cv2.HoughLinesP(edges, 1, np.pi / 180, threshold=50, minLineLength=30, maxLineGap=10)

        if lines is not None:
            # قم برسم مستطيل أخضر حول الجوال المكتشف
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # احفظ الصورة مع المستطيل الأخضر
            cv2.imwrite("result.jpg", image)

            # أرسل الصورة المعدلة إلى المستخدم
            with open("result.jpg", 'rb') as result_file:
                bot.send_photo(message.chat.id, result_file, "تم إلتقاط صورة لشخص يحمل الجوال")

            return

    # إذا لم يتم العثور على شخص يحمل جوال
    bot.reply_to(message, "لم يتم العثور على شخص يحمل جوال في الصورة.")

if __name__ == "__main__":
    bot.polling(none_stop=True)
