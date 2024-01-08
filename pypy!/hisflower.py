import telebot

# قم بتبديل 'YOUR_BOT_TOKEN' برمز البوت الخاص بك على تيليجرام الفعلي
bot = telebot.TeleBot('6340761111:AAGT_2Jk15CPMk3duO8AXFgSZJDNWjMiEMU')

@bot.message_handler(func=lambda message: message.text == 'I love you')
def sf(message):

        # قم بتبديل 'path/to/flower_image.jpg' بالمسار الفعلي لصورة الزهرة الخاصة بك
        with open('imgi.jpg', 'rb') as photo:
            bot.send_photo(message.chat.id, photo, caption='Me too!!')



# قم بتشغيل البوت
bot.polling()
