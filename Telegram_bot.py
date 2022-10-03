import telebot
bot = telebot.TeleBot('5505884222:AAEV1nCPYqoaYYTILJBkps_XVrgcCHyq5AE')

@bot.message_handler(content_types=['text', 'document', 'audio'])
def get_text_messages(message):
    if message.text == "Привет":
        bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")

    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Напиши 'привет' или 'эй ты бот расскажи анекдот'")

    elif message.text == 'эй ты бот расскажи анекдот':
        bot.send_message(message.from_user.id, 'ах ты так, твои мозги еще далеки до моих нейронов , '
                                                'а знал бы ты кто меня зделал... ты бы был в шоке')

    else:
        bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

bot.polling(none_stop=True, interval=0)