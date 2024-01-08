import telebot

bot= telebot.TeleBot('6340761111:AAGT_2Jk15CPMk3duO8AXFgSZJDNWjMiEMU')

@bot.message_handler(func=lambda message: message.text.l() =='ily'or'i love you')

def sf(message):

        with open('imgi.jpg','rb') as photo:
            bot.reply_to(message,"Me too samiri!")
            bot.send_photo(message.chat.id,photo,caption='')
        with open('1000155345.jpg','rb') as photo1:
            bot.send_photo(message.chat.id,photo1,caption='كيف بسس')

if __name__ == "__main__":
    bot.polling(none_stop=True)